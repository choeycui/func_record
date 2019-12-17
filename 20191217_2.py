# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:21:16 2019

This code is used to go through all the ways split a list by applying the baffle plate.

@author: choeycui
"""

list2besplited = [1,2,3,4]

# this function is used to get all the subset of a set
def PowerSetsBinary(items):
    N = len(items)
    set_all = []
    for i in range(1,2**N):
        combo = []
        for j in range(N):
            if (i>>j)%2 ==1:
                combo.append(items[j])
        set_all.append(combo)
    return set_all

def listsplit(items,slices):
    all_combo = []
    for i in range(len(slices)):
        sliceway = []
        sliceway.append(items[0:slices[i][0]])
        for j in range(len(slices[i])-1):
            sliceway.append(items[slices[i][j]:slices[i][j+1]])
        if slices[i][-1] != len(items):
            sliceway.append(items[slices[i][len(slices[i])-1]:])
        all_combo.append(sliceway)
    return all_combo
    
slices = list(range(1,len(list2besplited)+1))
all_ = PowerSetsBinary(slices)

lists = listsplit(prov,all_)
