#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[155]:


# using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations

cars = pd.read_csv('cars.csv')
cars


# In[165]:


# a. display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

# combine two operations which are slicing and using .head()
# [1::2], so that it will begin at 1 and will increment by 2 to obtain the odd number of rows
# .head() to return the first five rows
cars[1::2].head()


# In[167]:


# b. display the row that contains the ‘Model’ of ‘Mazda RX4’.

# use .loc to extract the row and column containing the Model which is Mazda RX4
cars.loc[[0],['Model']]


# In[169]:


# c. how many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

# use .loc to extract the value under 'cyl' and display the name Camaro Z28
cars.loc[[23],['Model','cyl']]


# In[171]:


# d. determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# use .loc to extract the values under 'cyl' and 'gear' of the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’
cars.loc[[1,28,18],['Model','cyl','gear']]


# In[ ]:




