# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 05:21:33 2019

@author: Administrator
"""
def recur_fact(n):
    if n==1:
        return n
    elif n==0:
        return 1
    else:
        return n*recur_fact(n-1)
while True:
    try:
        n1,n2=map(int,input().split())
        n1=recur_fact(n1)
        n2=recur_fact(n2)
        print(n1+n2)
    except:
        break