#!/usr/bin/env python
# coding: utf-8

# # Assignment 6: Dictionary

# In[14]:


list1 = [1,2,3,4,5,6,7,8]
list2 = ["a","b","c","d","e"]
len_d = min(len(list1), len(list2))
dict_d = {}

# print([ dict_d [ list1[each] ] = list2[each] for each in range(len_d) ])
print({list1[(i+1)-1]: list2[i] for i in range(len_d) })
# print(list(zip(list1, list2)))

