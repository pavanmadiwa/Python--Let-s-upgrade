#!/usr/bin/env python
# coding: utf-8

# # Assignment 7:

# In[6]:


#Question 1:
port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}
print(port1)
          
port2 = {value: key for key, value in port1.items()}
print(port2)
          


# In[61]:


#Question 2:
#Method 1:
# l1 = [(1,2), (3,4), (5,6),(4,5)]
# res= print([l1[0][0]+l1[0][1], l1[1][0]+l1[1][1], l1[2][0]+l1[2][1]])    

#Method 2:
l1 = [(1,2), (3,4), (5,6),(4,5)]

res = sum(i[0] for i in l1), sum(i[1] for i in l1)
print(res)
       

