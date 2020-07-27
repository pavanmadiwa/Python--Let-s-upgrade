#!/usr/bin/env python
# coding: utf-8

# # Assignment 4: Strings

# In[5]:


#Question 1:
import re
str1 = "what we think we become; we are Python programmer"
sub_str1 = "we"

print("original string is: " + str1)
print("Sub string to find is: "+ sub_str1)

indices = [i.start() for i in re.finditer(sub_str1, str1)]

print("Indices of substring found at: ", str(indices))


# In[13]:


#Question 2: isUpper(), islower()
str_upper = "THIS IS TO CHECK LOWER CASE METHOD"

print(str_upper.islower())
print(str_upper.isupper())

str_lower = "This is to check upper case method"
print(str_lower.islower())
print(str_lower.isupper())

print(str_upper.lower())
print(str_lower.upper())

