#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Lab_Assignment 2 (Association Rule mining)
#Group Members: Aggrim Sharma, Jagrati Tyagi, Onish Garg

import numpy as np
import pandas as pd
from apyori import apriori 


# In[3]:


store_data = pd.read_csv('Dataset.csv', header=None)


# In[4]:


store_data


# In[5]:


store_data.shape


# In[6]:


#converting pandas dataframe into a list of lists
records = []
for i in range(0,65500):
    records.append([str(store_data.values[i,j]) for j in range(0,3)])


# In[7]:


#to build apriori model
association_rules = apriori(records, support=0.50, confidence=0.7, lift=1.2, length=2)
association_results = list(association_rules)


# In[8]:


#to print the number of rules
print(len(association_results))


# In[9]:


print(association_results)


# In[ ]:




