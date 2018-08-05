#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 14:48:53 2018

@author: sjeet
"""

import numpy as np
import matplotlib.pyplot as plt

def make_list():
    x=list(input('Provide array of numbers (Provide space between numbers)'))
    blank=''
    for i in x:
        blank=blank+i
    x_list=[]
    for i in blank.split(' '):
        x_list.append(int(i)) 
    return x_list

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
        if i==b:
            res.append(1)
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
        if b<=i<=c:
            res.append(1)
        if c<i<d:
            res.append((d-i)/(d-c))
    return res

def gauss_mf(x,c,s):
    res=[]
    for i in x:
        res.append(np.exp((-1/2)*((i-c)/s)**2))
    return res

def gen_bell(x,a,b,c):
    res=[]
    for i in x:
        res.append(1/(1+(i-c)/a)**(2*b))
    return res

def sigmoid(x,a,c):
    res=[]
    for i in x:
        res.append(1/(1+np.exp(-a*(x-c))))
    return res

def main():
    x=np.array(make_list())
    atm=int(input('Press 1 for triangular membership function or 2 for trapezoidal membership function 3 for Gaussian MF, 4 for generalised bell MF, 5 for sigmoid.'))
    if atm==1:
        print('Enter list of a,b,c.')
        b=make_list()
        res_ans=tri_mf(x,b)
    if atm==2:
        print('Enter list of a,b,c,d.')
        b=make_list()
        res_ans=trap_mf(x,b)
    if atm==3:
        print('Enter mean and sd for Gaussian MF')
        c=float(input('Value of mean '))
        s=float(input('Value of standard deviation '))
        res_ans=gauss_mf(x,c,s)
    if atm==4:
        print('Enter values of a,b,c')
        a=float(input('Value of a '))
        b=float(input('Value of b '))
        c=float(input('Value of c '))
        res_ans=gen_bell(x,a,b,c)
    if atm==5:
        print('Enter values of a,c')
        a=float(input('Value of a '))
        c=float(input('Value of c '))
        res_ans=sigmoid(x,a,c)
    else:
        print('Invalid input.')
    print('Your desired output is '+'\n',res_ans)
    print('\n'+'Plot is given below.'+'\n')
    plt.plot(res_ans)
    return res_ans
    
if __name__=='__main__':
    main()