
# coding: utf-8

# In[113]:

import re
from operator import itemgetter

def answer(string, terms):

    # sort terms alphabetically
    terms = sorted(terms)
    
    # Get occurence of each term
    indexes = []
    for term in terms:
        i = -1
        idx = []
        regex = re.compile('{0}( |$)'.format(term))
        substr = string # to allow rematching
        pos = 0

        while True:
            i = regex.search(string, pos=pos)      

            # If there's a match
            if i is not None:
                indexes.append({'start': i.start(), 'end': i.end(), 'term': term})
                pos = i.start() + 1
            else: # No match found
                break
    
    # sort indexes
    if len(indexes) == 0:
        return ''
    else:
        indexes = sorted(indexes, key=itemgetter('start'))
    
    # build substrings
    sub_strings = []
    for idx, i in enumerate(indexes):
        start = i
        # print 'START', idx, start
        used = [start['term']]
        
        for idk, j in enumerate(indexes[idx + 1:]):
            if j['term'] in used:
                pass
            else:
                used.append(j['term'])
            
            if sorted(used) == terms:
                end = j
                sub_strings.append([start, end])
                print start, end

    if sub_strings == []:
        return ''
    else:
        strings = []
        for s in sub_strings:
            str = string[s[0]['start']:s[1]['end']]
            str = str.strip()
            strings.append(str)

        # sort substrings by length
        strings = sorted(strings, key=lambda x: len(x))

        return strings[0]


# In[114]:

string = "many google employees can program well"
terms = ['google', 'program']
d = answer(string, terms)
d


# In[115]:

string2 = "these are the days of our lives days of wonder"
terms2 = ['days', 'wonder']
d2 = answer(string2, terms2)
d2


# In[116]:

string3 = "many google employees can goo program google and goo"
terms3 = ['goo', 'employees', 'hazel']
d3 = answer(string3, terms3)
d3


# In[117]:

string4 = "a b c d a"
terms4 = ["a", "c", "d"]
d4 = answer(string4, terms4)
d4


# In[ ]:



