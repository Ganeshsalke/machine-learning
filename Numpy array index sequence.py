#!/usr/bin/env python
# coding: utf-8

# In[1]:


#NUMPY ARRAY INDEX SEQUENCED


# In[2]:


import numpy as np


# In[3]:


arr=np.arange(10)


# In[4]:


arr


# In[10]:


arr[2:6]


# In[11]:


arr[:2]


# In[12]:


arr[:9]


# In[13]:


arr[8:]


# In[14]:


arr[1:7]


# In[15]:


arr[0:8]


# In[16]:


arr[2:8]=100


# In[17]:


arr


# In[23]:


arr[0:6]=99


# In[19]:


arr


# In[20]:


#2D array 


# In[35]:


arr_2D=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])


# In[36]:


arr_2D


# In[37]:


arr_2D[0:3]


# In[40]:


arr_2D[1,1]


# In[41]:


arr_2D[0,0]


# In[43]:


arr_2D[1,2]


# In[45]:


array=np.arange(0,11)


# In[46]:


array


# In[47]:


array>5


# In[48]:


array<7


# In[49]:


array[array>5]


# In[50]:


array[array<7]


# In[62]:


arra=np.arange(50).reshape(5,10)


# In[63]:


arra


# In[64]:


arra[1:3]


# In[ ]:


arra[:10]

