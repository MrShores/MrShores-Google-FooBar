
# coding: utf-8

# In[1]:

for x in range(1,12):
    print ((x+0)/3**0)%3


# In[2]:

for x in range(1,12):
    print ((x+1)/3**1)%3


# In[3]:

for x in range(1,27):
    print ((x+4)/3**2)%3


# In[4]:

for x in range(1,27):
    print ((x+13)/3**3)%3


# In[83]:

def answer(x):
    list = [] 
    expsum = 0

    # left vs right of the balance
    b = {
        'left': x,
        'right': 0,
    }
    for e in range(0, 40):
        mod = ((x + expsum)/3**e)%3

        if mod == 1:
            list.append('R')
            b['right'] = b['right'] + 3**e
        elif mod == 2:
            list.append('L')
            b['left'] = b['left'] + 3**e
        else:
            if b['left'] == b['right']:
                return list
            else:
                list.append('-')
        
        expsum = expsum + 3**e

    return list


# In[84]:

def get_number(list):
    print list
    sum = 0
    print 'length:', len(list)
    for e in range(0,len(list)):
        print 'e:', e
        if list[e] == 'R':
            sum = sum + 3**e
        elif list[e] == 'L':
            sum = sum - 3**e
    return sum


# In[85]:

list = answer(1)
get_number(list)


# In[86]:

list = answer(2)
get_number(list)


# In[87]:

list = answer(8)
get_number(list)


# In[88]:

list = answer(4)
get_number(list)


# In[89]:

list = answer(29)
get_number(list)


# In[90]:

answer(30)


# In[91]:

answer(32)


# In[92]:

answer(43)


# In[93]:

list = answer(1000000000)
get_number(list)


# In[41]:




# In[ ]:



