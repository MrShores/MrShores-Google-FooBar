
# coding: utf-8

# In[3]:

dict1 = ["y", "z", "xy"]   # y z x
dict2 = ["ba", "ab", "cb"] # b a c
dict3 = ["z", "yx", "yz"]  # x z y


# In[14]:

import difflib

def answer(words):
#     # get unique letters
#     unique = []
#     for w in words:
#         for i in range(0,len(w)):
#             if w[i] not in unique:
#                 unique.append(w[i])
    
#     # sort to use for comparison
#     unique = sorted(unique)

    map = [] # holds pairs of ordered words
       
    for i in range(0, len(words)-1):
        w1 = words[i]
        w2 = words[i+1]
        print 'WORDS:', w1, w2
        
         # compare letters up to shortest words
        for j in range(0, min(len(w1), len(w2))):
            print '    LETTERS:', w1[j], w2[j]

            if w1[j] != w2[j]: # if letters are different, then first word letter is first
                map.append([w1[j], w2[j]]) # ordered pairs
                break
    
    print 'MAP:', map
    
#     order = [] # start with first pair of ordered letters
#     order.append(map.pop(0))
#     while map:
#         if map[0][1] == order[0][0]:
#             order = [map[0]] + order
#             print order
#             map.pop(0)
#         elif map[0][0] == order[0][1]:
#             order = order.append(map.pop(0))
#             print order
            
#     print 'ORD:', order
    
    # for i in range(0, len(map)-1):
        
            
    # get w.1, first letter of first word
    # add it to list
    # get w.1, if first letter same as first, get 2nd letters
    # if same, get 3rd letters...

    
#     # order the letters by appearance
#     map = {n: [] for n in range(0,50)}
#     for w in words:
#         for i in range(0, len(w)):
#             map[i].append(w[i])

#     map = [map[n] for n in range(0,50) if len(map[n]) > 0]


#     # reduce duplicates from list, retain order of appearance
#     for i, m in enumerate(map):
#         reduced = []
#         for n in m:
#             if n not in reduced:
#                 reduced.append(n)
#         map[i] = reduced
    
#     print 'MAP:', map
    
#     # test if one map is the full set
#     for m in map:
#         if sorted(m) == unique: # first letters give full order
#             return m

#     pos = []
    
        
#     for i in range(0, len(map) - 1):
#         s = difflib.SequenceMatcher(None, map[i], map[i+1])

#         codes = s.get_opcodes()
        
#         merged = []
#         for c in codes:
#             if c[0] == 'insert':
#                 j1 = c[3]
#                 merged.append(map[i+1][j1]) # insert term from second list
#             else:
#                 i1 = c[1]
#                 merged.append(map[i][i1]) # insert term from first list

#         # if merged has all the unique letters, done!
#         if sorted(merged) == unique:
#             return merged
#         else:
#             map[i] = merged

    return map


# In[15]:

answer(dict3)


# In[16]:

answer(dict1)


# In[17]:

answer(dict2)


# In[18]:

# answer(['abc', 'aiajak', 'aza', 'defgh', 'llmn', 'nop', 'pqbrbs', 'tuvwx', 'yyyyy'])
answer(['j','kk','ka', 'ca', 'cc'])


# In[19]:

answer(['ab', 'aa', 'ac'])


# In[ ]:



