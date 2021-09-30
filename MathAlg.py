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

def inversa(matrix):#Shotout a Alfredo
    n = len(matrix)
    m = matrix
    
    for i in range(n):
        for j in range(n):
            if i==j:
                m[i].append(1)
            else:
                m[i].append(0)
                
    for i in range(n):
        if i!= j:
            ratio = m[j][i] / m[i][i]
                
            for k in range(2*n):
                m[j][k] = m[j][k] - ratio * m[i][k]
            
    for i in range(n):
        div = m[i][i]
        for j in range(2*n):
            m[i][j] = m[i][j]/div
            
    result = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n, n*2):
            result[i].append(m[i][j])
            
    return result

def normal():
    pass