#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 01:23:53 2019

@author: thonia
"""
n=list(map(int,input().strip().split()))
a,b,c=n
m1=(a+b+abs(a-b))/2
m2=int((m1+c+abs(m1-c))/2)
print('{} eh o maior'.format(m2))