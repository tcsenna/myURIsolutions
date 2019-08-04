#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 03:30:22 2019

@author: thonia
"""

c1,n1,p1=map(float,input().split())
c2,n2,p2=map(float,input().split())
price=n1*p1+n2*p2
print('VALOR A PAGAR: R$ {:.2f}'.format(price))