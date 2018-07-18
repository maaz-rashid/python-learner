
#%%
import pandas as pd
data = pd.read_csv("data/donations.csv")
#data.head()
data.dateAdded.head()
#%%
data.dateAdded = pd.to_datetime(data.dateAdded, format='%Y-%m-%dT%H:%M:%S')
data.dateAdded.head()

#%%
data.dateAdded = data.dateAdded.apply(lambda x: x.replace(microsecond=0))
#data.dateAdded
data.dateAdded.head()
#%%
data.dateAdded = pd.DatetimeIndex(data.dateAdded)
#data.set_index('dateAdded', inplace=True)
data.set_index('dateAdded').head()
data.columns
#data.head()
#%%
data.plot(x=data.dateAdded)