#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = 6
if num % 2 == 0:
    print("even")
else:
    print("odd")


# In[2]:


num = 3
result = "Positive" if num > 0 else ("Negative" if num < 0 else "zero")
print(result)


# In[3]:


L = [1,2,3,4,5,6]
[2*x for x in L]


# In[4]:


L = [1,2,3,4,5,6]
[x for x in L if x%2 == 0]


# In[5]:


L = [1,2,3,4,5,6]
[x for x in L if x%2 != 0]


# In[7]:


#print the average value of  the list of numbers using list comprehension
L = [1,2,3,4,5,6]
avg = sum([x for x in L])/len(L)
print(avg)


# In[11]:


#Dictionary comprehension
d1 = {'kitty':[70,40,60,80], 'bannu':[66,77,88,99]}
d1


# In[12]:


d1 = {'kitty':[70,40,60,80], 'bannu':[66,77,88,99]}
{k:sum(v)/len(v) for k,v in d1.items()}


# In[14]:


d1 = {'kitty':[70,40,60,80], 'bannu':[66,77,88,99]}
{k:sum(v)/len(v) for k,v in d1.items()}


# In[ ]:




