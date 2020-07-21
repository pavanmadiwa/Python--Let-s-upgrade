#!/usr/bin/env python
# coding: utf-8

# # Assignment 2: 
# a. Basic python syntax:

# In[2]:


#Ritual:
print("Hello beautiful world")


# In[4]:


print("This is a back slash \ character ")


# In[5]:


print("Welcome python")


# In[7]:


print("This is my the use of \"backslash\" character")


# In[10]:


print("""This is an instance of a triple quotes 
Hey here is the difference
""")


# In[11]:


"""
this notebook was created by me
"""


# In[12]:


print('usage of single quotes')


# In[13]:


print("usage \t of escape \n sequence")


# In[16]:


name = 'mickey mouse'
age = 10
salary = 20000

print("Disney famous cartoon character is", name,"age is", age, "salary is", salary)


# In[17]:




print("Disney famous cartoon character is %s age is %d salary is %d" %(name, age, salary))


# In[18]:


""" Variable assignment"""
a = 20
b = 12
print(a)
print(b)


# In[19]:


print(id(a))
print(id(b))


# In[20]:


x = y = z = 50
print(x)
print(y)
print(id(y))


# In[21]:


del(x)
print(x)
print(y)


# In[22]:


print(y)


# In[23]:


"""Operators"""
a = 50
b = 10
c= 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**c)
print(a^c)


# In[30]:


x = 20
y = 10
print(x == y)
print(x > y)
print(x < y)
print(x <= y)
print(x >= y)
print(x!= y)
 


# In[31]:


print(x = !y)


# In[33]:


x = 20
y = 10
print(x & y)
print(x | y)
print(~x)
print(~y)


# In[34]:


print(bin(a))


# In[37]:


x = 30
y = 15
print(x and y)
print(x or y)


# In[44]:


p = 10

print(10 > 9 and p >= 10)
print(10 < 9 and p >= 11)


# In[46]:


n = 20

print(10 < 9 or n > 10)
print(10 > 9 or n <= 10)


# In[47]:


""" precedence rule"""

print(15+3/2-1*15/11//20)


# In[48]:


a = -2
b = 266
c = 266
print(a is b)
print(a is not c)
print(b is c)


# In[54]:


str = "karna was a good friend"
str1 = "friend"
# str1 in str
print(str not in str1)


# In[56]:


s = t = 266

print(id(s))
print(id(t))

