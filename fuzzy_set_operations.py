#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:24:52 2018

@author: sjeet
"""
import numpy as np

#%%
def sum_det(a,b):
    ak=list(a.keys())
    bk=list(b.keys())
    dic={}
    for i in ak:
        c1=a[i]
        for j in bk:
            abk=(i,j)
            c2=b[j]
            dic[abk]=max(c1,c2)
    return dic

def cartesan_prod(a,b):
    ak=list(a.keys())
    bk=list(b.keys())
    dic={}
    for i in ak:
        c1=a[i]
        for j in bk:
            abk=(i,j)
            c2=b[j]
            dic[abk]=min(c1,c2)
    return dic

def union(a,b):
    ak=list(a.keys())
    bk=list(b.keys())
    tot_k=list(np.unique(ak+bk))
    dic={}
    for i in tot_k:
        if i not in ak:
            c1=0
            c2=b[i]
        if i not in bk:
            c2=0
            c1=a[i]
        if i in ak and i in bk:
            c1=a[i]
            c2=b[i]
        dic[i]=max(c1,c2)
    return dic

def intersection(a,b):
    ak=list(a.keys())
    bk=list(b.keys())
    tot_k=list(np.unique(ak+bk))
    dic={}
    for i in tot_k:
        if i not in ak:
            c1=0
            c2=b[i]
        if i not in bk:
            c2=0
            c1=a[i]
        if i in ak and i in bk:
            c1=a[i]
            c2=b[i]
        dic[i]=min(c1,c2)
    return dic

def diff_set(a,b):
    ak=list(a.keys())
    bk=list(b.keys())
    dic={}
    for i in ak:
        if i not in bk:
            dic[i]=a[i]
    return dic

def set_complement(a):
    dic={}
    for i in list(a.keys()):
        dic[i]=1-a[i]
    return dic

#%%
def str_to_dict(dic_str):
    ds=dic_str[1:-1]
    ds=ds.split(',')
    dic={}
    for i in ds:
        t=i.split(':')
        k=t[0]
        v=float(t[1])
        dic[k]=v
    return dic

def check_keys(dic_str):
    flag=False
    ds=dic_str[1:-1]
    ds=ds.split(',')
    dl=[]
    for i in ds:
        t=i.split(':')
        dl.append(t[0])
    if len(np.unique(dl))!=len(dl):
        flag=True
    return flag

def main():
    print('Enter two fuzzy sets for set operations.')
    ass=input('Enter 1st fuzzy set in dictionary format. ')
    bs=input('Enter 2nd fuzzy set in dictionary format. ')
    fl=check_keys(ass) or check_keys(bs)
    if fl:
        ans= 'Duplicate keys found. Try again.'
    else:
        a=str_to_dict(ass)
        b=str_to_dict(bs)
        kt=int(input('Enter 1 for co-cartesan product, 2 for cartesan product, 3 for union, 4 for intersection, 5 for set difference, 6 for finding complement. '))
        if kt==1:
            ans=sum_det(a,b)
        if kt==2:
            ans=cartesan_prod(a,b)
        if kt==3:
            ans=union(a,b)
        if kt==4:
            ans=intersection(a,b)
        if kt==5:
            ans=diff_set(a,b)
        if kt==6:
            print('Showing set complement of 1st set')
            ans=set_complement(a)
        if kt not in [1,2,3,4,5,6]:
            print('Invalid input.')
    return print(ans)

if __name__=='__main__':
    main()