# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 04:46:42 2021

@author: Usuario
"""

  
def facto(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
        
    return fact
    
def permu(n, r):
     perm = facto(n)/facto(n-r)
     return perm
 
def combin(n, r):
    comb = facto(n)/(facto(r)*facto(n-r))
    return comb
    
x = permu(7,5)
y = combin(5,2)
z = facto(4)
print(x)

