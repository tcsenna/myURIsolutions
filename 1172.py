# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 05:27:39 2019

@author: Administrator
"""

X=[]
for i in range(10):
    a=int(input())
    if(a<=0):
        a=1
        X.append(a)
    else:
        X.append(a)
    print("X[{}] = {}".format(i,a))
    