#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 14:48:53 2018

@author: sjeet
"""

import numpy as np
import matplotlib.pyplot as plt
def tri_mf(x,defn):
    a=defn[0]
    b=defn[1]
    c=defn[2]
    res=[]
    for i in x:
        if i<=a or i>=c:
            res.append(0)
        if a<i<b:
            res.append((i-a)/(b-a))
        if b<i<c:
            res.append((c-i)/(c-b))
    return res

def trap_mf(x,defn):
    a=defn[0]
    b=defn[1]
    c=defn[2]
    d=defn[3]
    res=[]
    for i in x:
        if i<=a or i>=d:
            res.append(0)
        if a<i<b:
            res.append((i-a)/(b-a))
        if b<i<c:
            res.append(1)
        if c<i<d:
            res.append((d-i)/(d-c))
    return res

def make_list():
    x=list(input('Provide array of numbers (Provide space between numbers)'))
    blank=''
    for i in x:
        blank=blank+i
    x_list=[]
    for i in blank.split(' '):
        x_list.append(int(i)) 
    return x_list

def main():
    x=np.array(make_list())
    a=int(input('Press 1 for triangular membership function or 2 for trapezoidal membership function.'))
    if a==1:
        print('Enter list of a,b,c.')
        b=make_list()
        res_ans=tri_mf(x,b)
    if a==2:
        print('Enter list of a,b,c,d.')
        b=make_list()
        res_ans=trap_mf(x,b)
    print('Your desired output is '+'\n',res_ans)
    print('\n'+'Plot is given below.'+'\n')
    plt.plot(res_ans)
    
if __name__=='__main__':
    main()
