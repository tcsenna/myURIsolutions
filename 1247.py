# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 06:02:06 2019

@author: Administrator
"""

while True:
    try:
        d,vf,vg=map(int,input().split())
        tf=12/vf
        tg=((12**2+d**2)**(0.5))/vg
        if tg>tf:
            print('N')
        else:
            print('S')
    except:
        break
    