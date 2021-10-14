# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:52:47 2021

@author: Elean Rivas
"""

#Libreria matemáticas alg lineal
import collections

V2 = collections.namedtuple('Point2', ['x', 'y'])
V3 = collections.namedtuple('Point3', ['x', 'y', 'z'])
V4 = collections.namedtuple('Point4', ['x', 'y', 'z', 'w'])


def dotProduct(a, b):
    x = (a.x * b.x + a.y * b.y + a.z * b.z)     
    return x

def crossProduct(a, b):
    x = a.y * b.z - a.z * b.y
    y = a.z * b.x - a.x * b.z
    z = a.x * b.y - a.y * b.x

    return V3(x,y,z)

def add(a, b):
    x = a.x + b.x
    y = a.y + b.y
    z = a.z + b.z
    return V3(x,y,z)

def substract(a, b):
    x = a.x + b.x
    y = a.y + b.y
    z = a.z + b.z
    return V3(x,y,z)

def multiply(a, b):
    x = a.x * b.x
    y = a.y * b.y
    z = a.z * b.z
    return V3(x,y,z)

def vector_Scalar(a, k):
    x = a.x *k
    y = a.y *k
    z = a.z *k
    return V3(x,y,z)

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

def magnitude(v):
    return (v[0]**2 + v[1]** + v[0]**2)**0.5

def normal(a):
    #Vector normal
    l = magnitude(a)
    if l == 0:
        return V3(0, 0, 0)
    else:
        return V3(a.x/l, a.y/l, a.z/l)
    
def matrixMul(a,b):
    #Multiplicacion de matrices 
    if len(a[0]) == len(b):
        resultMatrix = [[0] * len(b[0]) for i in range(len(a))]
        for x in range(len(a)):
            for y in range(len(b[0])):
                for z in range(len(a[0])):
                    try:
                        resultMatrix[x][y] += a[x][z] * b[z][y]
                    except IndexError:
                        pass
        return resultMatrix
    else:
        print("\nERROR: No es una matriz cuadrada")
        return 0
    