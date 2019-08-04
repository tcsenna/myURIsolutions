#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 01:03:59 2019

@author: thonia
"""

n=int(input())
anos=int(n/365)
n1=n%365
meses=int(n1/30)
dias=n1%30
print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))