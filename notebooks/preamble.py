%matplotlib inline
#NB I open a standard set of directories

#Paths

#Get the top path
top_path = os.path.dirname(os.getcwd())

#Create the path for external data
ext_data = os.path.join(top_path,'data/external')

#Raw path (for html downloads)

raw_data = os.path.join(top_path,'data/raw')

#And external data
proc_data = os.path.join(top_path,'data/processed')

fig_path = os.path.join(top_path,'reports/figures')

#And the model path
mod_path = os.path.join(top_path,'models/')

#Get date for saving files
today = datetime.datetime.today()

today_str = "_".join([str(x) for x in [today.day,today.month,today.year]])