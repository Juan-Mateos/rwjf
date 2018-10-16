import sys
sys.path.append('../src/')
from text_preprocessing import *
from utils import *

df = pd.read_csv('../data/raw/gh_cb_gdb_v1.csv', compression='gzip')
df.reset_index(inplace=True, drop=True)

# add 'github' in front of repo ID
df['Row ID'] = ['_'.join(['github', str(df.loc[i, 'Row ID'])]) 
                if df.loc[i, 'Source ID'] == 'GitHub' else df.loc[i, 'Row ID'] 
                for i in range(df.shape[0])]

# keep rows with description
df = df[df['Description'].isnull()==False]

# Dropping duplicates in v2 because the dataset is on ORG level
df.drop_duplicates('Row ID', inplace=True)
df.reset_index(inplace=True, drop=True)

# Instantiate textpreprocessing
nlproc = TextPreprocessing()

def rwjf_sent(text):
    """Remove first sentence of RWJF grants."""
    txt = []
    for sent in text.split('.'):
        if ':' in sent:
            txt.extend(sent.split(':'))
        else:
            txt.append(sent)
    if len(txt) > 1:
        return '. '.join(txt[1:])
    else:
        return ' '.join(txt)


df['Description'] = [desc if df.loc[i, 'GDB Dataset ID'] != 'rwjf' else rwjf_sent(desc) for i, desc in enumerate(df['Description']) ]

# Preprocess descriptions
documents = [flatten_lists(nlproc.tokenize_document(doc)) for doc in list(df['Description'])]

# bigrams
docs = nlproc.bigrams(documents)