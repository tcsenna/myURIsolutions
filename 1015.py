#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 17:24:08 2019

@author: thonia
"""
import math 
a=input().split()
b=input().split()
x1,y1=a
x2,y2=b
k=[float(p) for p in [x1,y1,x2,y2]]
dist=math.sqrt((k[2]-k[0])**2+(k[3]-k[1])**2)
print("%0.4f" %dist)