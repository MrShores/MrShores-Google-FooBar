
# coding: utf-8

# In[41]:

x = [2.0, 6.0, 4.0]
y = [3.0, 2.0, 1.0]


# In[42]:

def answer(x,y):
    """
    Find the percent improvement between two floating
    point lists, rounded to the nearest integer.
    """     
    x = sorted(x)
    y = sorted(y)
    
    improvements = []
    for a,b in zip(x,y):
        diff = a - b
        percent = diff / a * 100
        percent = int(percent)
        improvements.append(percent)
        print percent

    return improvements[0]


# In[43]:

answer(x,y)


# In[44]:

# TEST CASE 1
x1 = [1.0]
y1 = [1.0]

answer(x1,y1)


# In[45]:

# TEST CASE 2
x2 = [23.0, 150.0, 1024.0, 34868.0]
y2 = [2.2999999999999998, 15.0, 102.40000000000001, 3486.8000000000002]

answer(x2,y2)


# In[ ]:



