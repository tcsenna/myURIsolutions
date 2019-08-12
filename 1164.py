# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 05:56:52 2019

@author: Administrator
"""

n=int(input())
for k in range(n):
    soma=0
    x=int(input())
    for i in range(1,x):
        if(x%i==0):
            soma+=i
    if(soma==x):
        print('{} eh perfeito'.format(x))
    else:
        print('{} nao eh perfeito'.format(x))