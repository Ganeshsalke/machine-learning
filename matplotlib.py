#!/usr/bin/env python
# coding: utf-8

# In[1]:


#DATA VISUALIZATION


# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


x=np.linspace(4,5,11)
y=x**2


# In[7]:


x


# In[8]:


y


# In[9]:


#ploting there are two methods will be present.
#1.functional method
#2.object oriented method


# In[10]:


#1.functional method


# In[11]:


plt.plot(x,y,'red',linestyle='--',linewidth='20')
plt.xlabel('zeal')
plt.ylabel('dyanu')
plt.title('ganesh')


# In[12]:


plt.subplot(1,3,1)
plt.plot(x,y,'blue',linestyle='--',linewidth='12')
plt.subplot(1,3,2)
plt.plot(x,y,'orange',linestyle='solid',linewidth='11')


# In[13]:


#2. object orinted method


# In[14]:


fig=plt.figure()
axes=fig.add_axes([0.1,0.3,0.4,0.7])

axes.plot(x,y)
axes.set_xlabel('gana')
axes.set_ylabel('salke')
axes.set_title('patil')


# In[15]:


fig=plt.figure()
axes1=fig.add_axes([0.1,0.1,0.8,0.8])
axes2=fig.add_axes([0.2,0.0,0.3,0.3])


# In[16]:


fig=plt.figure()
axes1=fig.add_axes([0.2,0.4,0.6,0.6])
axes2=fig.add_axes([0.1,0,0.2,0.3])
axes1.plot(x,y)
axes2.set_xlabel('haaaa')


# In[17]:


fig,axes=plt.subplots(figsize=(8,3),nrows=1,ncols=2)


# In[18]:


plt.plot(x,y)


# In[28]:


df=plt.figure()
axes=df.add_axes([1,3,2,1])
plt.plot(x,y,'red',linewidth=12)


# In[35]:


df=plt.figure()
axes1=df.add_axes([1,2,3,1])
axes2=df.add_axes([1,0,3,1])
axes1.plot(x,y,'red','',linewidth=12)
axes2.plot(x,y,'green',linewidth=12)


# In[ ]:





# In[ ]:




