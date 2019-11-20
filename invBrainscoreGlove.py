#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Load the results file in the brainmodeling env from openmind

import pickle

with open('benchmark=Pereira2018-encoding-min,model=glove,subsample=None,bold_shift=4.pkl', 'rb') as f:  
    result = pickle.load(f)


# In[3]:


print(result)


# In[14]:


print('Keys: ', result.keys(), '\n \nValues: ', result.values())


# In[15]:


data = result['data']


# In[16]:


data


# In[19]:


data.raw


# In[21]:


# Score results

data[0]


# In[22]:


data[1]


# In[ ]:





# In[ ]:




