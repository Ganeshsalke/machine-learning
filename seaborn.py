#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Seaborn
#seaborn is python liberary it will uses for the visulised ststistical data it is called as seaborn.
#1.simple 
#2.categorical
#3.matrix
#linear


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


sn=pd.read_csv('collegePlace.csv')


# In[6]:


sn


# In[7]:


sn.head()


# In[8]:


sn.tail()


# In[9]:


sn.isnull()


# In[10]:


sn[sn==0]


# In[11]:


sn.shape


# In[12]:


sn.columns


# In[13]:


sn.index


# In[14]:


sn.nunique()


# In[15]:


sn['Age'].count()


# In[16]:


sn['Age']==0


# In[17]:


sn.dtypes


# In[18]:


sn


# In[19]:


sn['Stream']


# In[20]:


sn[sn['Stream']=='Information Technology']


# In[21]:


sn[sn[sn['Stream']=='Information Technology']=='Male']


# In[22]:


sn[sn['Internships']==0].count()


# In[23]:


sn[sn['Internships']==1].count()


# In[24]:


sn[sn['PlacedOrNot']==0].count()


# In[25]:


sn[sn['PlacedOrNot']==1].count()


# In[26]:


#visulization


# In[27]:


sns.distplot(sn['PlacedOrNot'])


# In[28]:


sns.distplot(sn['PlacedOrNot'],kde=False)


# In[29]:


sns.jointplot(x='Stream',y='HistoryOfBacklogs',data=sn)


# In[30]:


sn


# In[34]:


sns.pairplot(sn)


# In[35]:


#sns.rugplot(sn)


# In[36]:


sns.barplot(x='Stream',y='Internships',data=sn)


# In[37]:


sns.countplot(x='Internships',data=sn)


# In[38]:


#Vlolinplot(x='HistoryOfBacklogs',y='Stream',data=sn)


# In[39]:


sns.stripplot(sn['Age'])


# In[40]:


sns.barplot(sn)


# In[71]:


sns.violinplot(x='Age',y='Gender',data=sn)


# In[53]:


sn


# In[55]:


sns.violinplot(x='Internships',y='Gender',data=sn)


# In[60]:


sns.violinplot(x='PlacedOrNot',data=sn)


# In[76]:


sns.stripplot(x='Gender',y='Stream',data=sn,jitter=True)


# In[5]:


df=sn.corr()
sns.heatmap(df,annot=True)


# In[ ]:




