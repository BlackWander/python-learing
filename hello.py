#!/usr/bin/env python3
# -*- coding: utf-8 -*-

time=input('输入你每天的睡眠时间（h）：')
t=int(time)
if t>=8 and t<=10:
   print('你这个年纪你还睡得着觉啊')
elif t>10:
    print('你是猪吗')
else:
    print('没救了，准备后事吧')

input()

high=input('输入你的身高:')
height=input('输入你的体重：')
h1=float(high)
h2=int(height)
x=(h2)/h1**2
print(f'你的BMI指数是：{x:.1f}')
if x<18.5:
    print('过轻')
elif x>=18.5 and x<25:
    print('正常')
elif x>=25 and x<28:
    print('过重')
elif x>=28 and x<32:
    print('肥胖')
else:
    print('严重肥胖')

