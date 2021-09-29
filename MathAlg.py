# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:52:47 2021

@author: Elean Rivas
"""

#Libreria matemáticas alg lineal

def dotProduct(a, b):
    c =()
    
    for i in len(a):
        x=a(i)*b(i)
        c.append(x)
        
    return sum(c)

def crossProduct(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c

def add(a, b):
    c =()
    
    for i in len(a):
        x=a(i)+b(i)
        c.append(x)
        
    return c

def substract(a, b):
    c =()
    
    for i in len(a):
        x=a(i)-b(i)
        c.append(x)
        
    return c

def multiply(a, b):
    c =()
    
    for i in len(a):
        x=a(i)*b(i)
        c.append(x)
        
    return c