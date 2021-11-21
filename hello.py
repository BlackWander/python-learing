#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def quadratic(a,b,c):
    delta=(b**2-4*a*c)
    if delta < 0:
        return('无解')
    else:
        x1=(-b+math.sqrt(b**2-4*a*c))/2*a
        x2=(-b-math.sqrt(b**2-4*a*c))/2*a
        return (x1,x2)

a,b,c=map(float,input('输入三个值,用空格键隔开：').split())
x,y= quadratic(a,b,c)
print(x,y)
