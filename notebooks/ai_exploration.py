
# coding: utf-8

# # Exploration of AI data for the RWJF project
# 
# Here we explore the AI data for the RWJF project. This involves:
# 
# * Analysing World Reporter
#   * Load
#   * Map
#   * Trend analysis
#   * MeSH exploration
#   
# * Consider other sources such as CrunchBase or GitHub to illustrate the range of sources we are working with.
# 
# 
# 

# ### World Reporter

# In[1]:


import boto3
import pandas as pd
from io import BytesIO

# bucket, filename = “innovation-mapping-general”, “nih_all_processed_data/all_processed_nih_10000.json”

# s3 = boto3.resource(‘s3’)
# obj = s3.Object(bucket, filename)
# with BytesIO(obj.get()[‘Body’].read()) as bio:
#    df = pd.read_csv(bio)


# In[2]:


# out= ''

# with open('../data/external/dloaded.txt','w') as outfile:
#     outfile.write(out)


# In[3]:


with open('../data/external/dloaded.txt','r') as infile:
    collected = infile.read().split(', ')


# In[4]:


collected


# In[5]:


dfs = {}


# In[ ]:


bucket = "innovation-mapping-general" 
directory = "nih_all_processed_data/" 
s3 = boto3.resource('s3') 

t=0
for key in s3.Bucket(bucket).objects.all(): 
    if not key.key.startswith(directory): 
        continue 
    if (key.key == directory): 
         continue
    
    if (key.key in collected):
        continue
    
    print(key)
    obj = s3.Object(bucket, key.key)     
    with BytesIO(obj.get()['Body'].read()) as bio:
        df = pd.read_json(bio) 
    dfs[key.key]=df
    
    collected.append(str(key.key))
    
    print(str(key.key))
    
    t+=1
    
    #Each five dfs, this saves the data as a timestamped df and the list with the collected data as a list
    if t%5==0:
        time = str(datetime.datetime.now())
        with open(f'../data/external/{time}_wtr.p','wb') as outfile:
            pickle.dump(list(dfs.values()),outfile)
        with open('../data/external/dloaded.txt','w') as outfile:
            outfile.write(', '.join(collected))
            
        del dfs
        dfs = {}
        
    
#df = pd.concat(dfs)     

