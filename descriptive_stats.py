#!/usr/bin/env python
# coding: utf-8

# In[7]:


#create a pandas series of batsman1 scores
import pandas as pd
s1 = [20,15,10,25,30,35,28,40,45,60]
scores1 = pd.Series(s1)
scores1


# In[19]:


import matplotlib.pyplot as plt
plt.boxplot(scores1, vert=False)


# In[45]:


#create a pandas series of batsman1 scores
import pandas as pd
s = [20,15,10,30,28,40,45,60,120,150]
scores1 = pd.Series(s)
scores1


# In[47]:


import matplotlib.pyplot as plt
plt.boxplot(scores1, vert=False)


# In[55]:


df = pd.read_csv("universities.csv")
print(df)
#plot box plot for SAT column
plt.boxplot(df["SAT"])


# In[ ]:




