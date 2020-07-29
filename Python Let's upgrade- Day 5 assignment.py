#!/usr/bin/env python
# coding: utf-8

# # Day 5: Assignment

# In[27]:


#Question 1:
# Funtion to move all zeros to end
def zerosToRight(list, n):
    count = 0
    
    for i in range(n):
        if list[i] != 0:
            list[count] = list[i]
            count += 1
        
    while count < n:
        list[count] = 0
        count+= 1
        
        
list = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
n = len(list)
zerosToRight(list, n)
print(list)


# newlist = 0
# for j in list:
#     if list[j] != 0:
#         list[newlist] = list[j]
#         newlist+= 1

#     else:
#         print('list has zero elements')
        
print(sorted(list))     
        


# In[26]:


#Question 2:
list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,60] 
# def mergeList(list1, list2): 
#     return [item for pair in zip(list1, list2 + [0]) 
#                                  for item in pair] 
 
# mergeList(list1, list2)   

for i in list2:
    list1.append(i)
    
print(list1)

