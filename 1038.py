#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 02:04:07 2019

@author: thonia
"""
#trabalhando com a entrada
n=input().split()
p,q=n
q=int(q)
d = {'1': 4, '2': 4.5, '3': 5,'4': 2, '5': 1.5}
total=q*(d.get(p))
print('Total: R$ {:.2f}'.format(total))