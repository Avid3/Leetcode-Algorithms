# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 13:52:21 2019

@author: Amey
"""
#mergesort
import random

def insertsort(arr):
#now for sorting
    i=0
    j=0
    s=0
    w=0
    for w in range(0,len(arr)):
        for j in range(0,len(arr)):
            for i in range(1,len(arr)):
                if int(arr[i])<int(arr[i-1]):
                    s=int(arr[i])
                    arr[i]=int(arr[i-1])
                    arr[i-1]=s
    
    return(arr)
s=random.randint(5,15)

i=0
w=[None]*int(s)
z=[None]*int(s)
for i in range(0,int(s)):
   w[i]=random.randint(0,100)
if s%2==0: 
    w_21=[None]*int(s/2)
    w_22=[None]*int(s/2)
if s%2!=0:
    w_21=[None]*(int(s/2)+1)
    w_22=[None]*(int(s/2))
if s%2!=0:
    i=0
    for i in range(0,int(s/2)+1):
        w_21[i]=w[i]
    i=0
    for i in range(0,int(s/2)):
        w_22[i]=w[int(s/2)+1+i]
        
if s%2==0:
    i=0
    for i in range(0,int(s/2)):
        w_21[i]=w[i]
    i=0
    for i in range(0,int(s/2)):
        w_22[i]=w[int(s/2)+i]
        

a=insertsort(w_21)
b=insertsort(w_22)
i=0
j=0
k=0
for k in range(0,int(s)+1):
    if a[i]<b[j]:
        z[k]=a[i]
        i=i+1
    else:
        z[k]=b[j]
        j=j+1

    

    
    