# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:07:29 2019

@author: Amey
"""
#remove specific element
def remove_val(arr,val):
  #  a=[None]*len(arr);
    
    while val in arr:
        arr.remove(val)
    
    
    return(arr)