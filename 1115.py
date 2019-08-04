#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 02:23:15 2019

@author: thonia
"""
#teste: calcular o angulo entre (2,2) e (1,0)
#import math

x1,y1=map(int,input().split())
while (x1!=0) and (y1!=0):
    if (x1>0):
        if y1>0:
            print('primeiro')
            x1,y1=map(int,input().split())
        else:
            print('quarto')
            x1,y1=map(int,input().split())
    else:
        if y1>0:
            print('segundo')
            x1,y1=map(int,input().split())
        else:
            print('terceiro')
            x1,y1=map(int,input().split())
        
    
    