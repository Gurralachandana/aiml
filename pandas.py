#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#create pandas series using list
data = [10, 20, 30, 40]
series = pd.Series(data)
print(series)


# In[3]:


#create pandas series using list(Str calls object)
data = [10, 20, 30, 'a']
series = pd.Series(data)
print(series)


# In[4]:


#Create series using a custom index
data = [10, 20, 30, 40]
i = ['A', 'B', 'C', 'D']
series = pd.Series(data, index=i)
print(series)


# In[6]:


#create series using dictionary
data = {'a': 20, 'b':30, "c":80}
series= pd.Series(data)
print(series)


# In[7]:


series.replace(80,70)


# In[18]:


#create series using numpy array
import numpy as np
data = np.array([100, 700, 400])
series = pd.Series(data, index=['a','b','c'])
print(series)                            


# ## pandas dataframe

# In[13]:


#create pandas dataframe from dictionary of lists
import pandas as pd
data = {"Name": ['Alice', 'Bob', 'Mary'], 'Age': [25,19,30], 'Country':["UK","AUS","IND"]}
df = pd.DataFrame(data)
print(df)


# In[15]:


#create padas dataframe from numpy array
import numpy as np
array = np.array([[1, 2, 3], [4, 5, 6], [8,9,7]])
print(array)
df=pd.DataFrame(array, columns=['A', 'B', 'C'])
print(df)


# In[ ]:




