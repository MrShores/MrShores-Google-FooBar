
# coding: utf-8

# In[4]:

dict1 = ["y", "z", "xy"]   # y z x
dict2 = ["ba", "ab", "cb"] # b a c
dict3 = ["z", "yx", "yz"]  # x z y


# In[40]:

import difflib

def answer(words):
    # get unique letters
    unique = []
    for w in words:
        for i in range(0,len(w)):
            if w[i] not in unique:
                unique.append(w[i])
    
    # sort to use for comparison
    unique = sorted(unique)

    map = [] # holds pairs of ordered words
   
    for i in range(0, len(words)-1):
        w1 = words[i]
        w2 = words[i+1]
        
         # compare letters up to shortest words
        for j in range(0, min(len(w1), len(w2))):
            if w1[j] != w2[j]: # if letters are different, then first word letter is first
                map.append([w1[j], w2[j]]) # ordered pairs
                break
      
    order = [] # start with first pair of ordered letters
    order.append(map.pop(0))
    
    while map:
        if map[0][1] == order[0][0]:
            order = [map[0]] + order
            map.pop(0)
        elif map[0][0] == order[0][1]:
            order.append(map.pop(0))

        mid = [p for o in order for p in o]
        compiled = []
        for m in mid:
            if m not in compiled:
                compiled.append(m)
        if sorted(compiled) == unique:
            return compiled
    
    return False


# In[41]:

answer(dict3)


# In[42]:

answer(dict1)


# In[43]:

answer(dict2)


# In[44]:

answer(['j','kk','ka', 'ca', 'cc'])


# In[45]:

answer(['ab', 'aa', 'ac'])


# In[ ]:



