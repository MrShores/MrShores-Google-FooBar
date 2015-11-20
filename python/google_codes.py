
# coding: utf-8

# In[1]:

x = ["foo", "bar", "oof", "bar"]


# In[6]:

def answer(x):
    distinct = []
    for str in x:
        if str not in distinct:
            distinct.append(str)
            distinct.append(str[::-1])
    return len(distinct) / 2


# In[7]:

answer(x)


# In[8]:

x1 = ["x", "y", "xy", "yy", "", "yx"]


# In[9]:

answer(x1)


# In[ ]:



