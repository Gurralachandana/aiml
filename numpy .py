#!/usr/bin/env python
# coding: utf-8

# In[6]:


#numpy array
import numpy as np
x = np.array([40,67,57,9.8])
print(x)
print(type(x))
print(x.dtype)


# In[7]:


x = np.array(["A",40,67,57,9.8])
print(x)
print(type(x))
print(x.dtype)


# In[9]:


a = np.array([10,20,30,40])
b = a.reshape(2,2)
print(b)
print(b.shape)


# In[10]:


a = np.array([10,20,30,40])
b = a.reshape(1,4)
print(b)
print(b.shape)


# In[13]:


#create an array with arange function
c = np.arange(3,32)
print(c)
type(c)


# In[14]:


d = np.array([1.345, 3.456, 4.8987])
np.around(d,2)


# In[18]:


a1 = np.array([[3,4,5,8],[7,2,8,np.NAN]])
print(a1)
a1.dtype


# In[20]:


a1_copy1 = a1.astype(str)
print(a1_copy1)
a1_copy1.dtype


# In[41]:


a2=np.array([[3,4,5],[7,2,8],[9,1,6]])
a2


# In[42]:


print(a2.sum(axis = 1))
print(a2.sum(axis=0))


# In[44]:


print(np.mean(a2, axis = 1))
print(np.mean(a2, axis=0))


# In[40]:


#matrix operations of array
a3=np.array([[3,4,5],[7,2,8],[9,1,6]])
print(a3)
np.fill_diagonal(a3,0)
print(a3)


# In[52]:


A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(A.T)
print(B.T)


# In[56]:


a4 = np.array([[3,4,5],[7,2,8],[9,1,6],[10,9,18]])
a4


# In[57]:


#slicing the array
a4[1:3,0:2]


# In[58]:


#slicing the array
a4[0:4,1:3]


# In[59]:


#slicing the array
a4[3:4,0:4]


# In[ ]:




