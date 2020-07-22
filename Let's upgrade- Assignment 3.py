#!/usr/bin/env python
# coding: utf-8

# # Assignment 3:
# 1. To find the sum of number using while loop
# 
# 2. To find wheather the number is prime or not

# In[9]:


"""To find the sum of a number using a while loop"""
sum = 0
r = eval(input("Enter the range of a number"))
while r != 0:
    sum = sum+r
    print(r,"-->", sum)
    r = r-1
print("Sum of the no is:", sum)
    


# In[21]:


"""To find wheather the number is prime or not"""
n = int(input("Enter the integer number to find prime or not "))

if n > 1:
    for i in range(2, n):
        if (n%i) == 0:
            print("Entered integer number is not a prime no")
            break
        else:
            print("Entered integer number is a prime no")
         
else:
    print("Entered number is not a prime number")

