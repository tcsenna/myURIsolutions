# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 06:32:12 2019

@author: Administrator
"""

while True:
    a,b=map(int,input().split())
    if (a!=0) and (b!=0):
        k=a+b
        lista=[]
        j=str(k)
        for i in j:
            if (i != '0'):
                lista.append(i)
        lista= int("".join(lista))
        print(lista)
    else:
        break
    