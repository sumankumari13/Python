#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
n=int(input('enter the number of numbers you want to find the sum'))
l=[]
sum=0
for i in range(10):
    m=random.randint(1,100)
    l.append(m)
    sum=sum+m
    
print('sum of the numbers',l,'is',sum)

