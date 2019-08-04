#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 20:46:52 2019

@author: thonia
"""

#import math
a,b,c=input().split()
n=[float(i) for i in [a,b,c]]
tri=(n[0]*n[2])/2
cir=3.14159*n[2]**2
tra=((n[0]+n[1])*n[2]/2)
qua=n[1]**2
ret=n[0]*n[1]
print("TRIANGULO: %0.3f" %tri)
print("CIRCULO: %0.3f" %cir)
print("TRAPEZIO: %0.3f" %tra)
print("QUADRADO: %0.3f" %qua)
print("RETANGULO: %0.3f" %ret)