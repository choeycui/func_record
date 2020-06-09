# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 17:10:55 2020

This File is to create a tree via a file of the relationship between the parent object and child object
(Please mark the root name with value == 1 in column 'ROOT')

@author: choeycui
"""

from collections import defaultdict
import pandas as pd
import pprint

def tree(): return defaultdict(tree)
def dicts(t): return {k: dicts(t[k]) for k in t}
def get_child(df, pmbd, pcol, ccol): return list(df[df[pcol]==pmbd][ccol].unique())

def add(t, path):
  for node in path:
    t = t[node]

def convert(x):
    try: 
        return eval('['+x[1:-1]+']')
    except:
        return None
    
class ObjName:
    def __init__(self, name, parent, ):
        self.name = name
        self.parent = parent

name_ref = pd.read_excel('YOUR FILE PATH',sheet_name = 'YOUR SHEET NAME')        
name_root = list(name_ref[name_ref['ROOT']==1]['CHILD'])
paths = [[i] for i in name_root]
name2obj = {}
nametree = tree()

for root in name_root:
    name2obj[root] = ObjName(root,None)
    nametree[root]
    
def tree_gen(df, pcol, ccol):
    for path in paths:
        if len(path) > 1:
            name2obj[path[-1]] = ObjName(path[-1],name2obj[path[-2]])
        children = get_child(df,path[-1],pcol,ccol)
        if len(children) == 0:
            add(nametree, path)
        else:
            path.append(None)
            for child in children:
               path[-1] = child
               tree_gen(df, pcol, ccol)
            path.pop()
            
# 'PARENT' IS THE COLUMN NAME OF PARENT NAME 
# 'CHILD' IS THE COLUMN NAME OF CHILD NAME 
tree_gen(name_ref,'PARENT','CHILD')            
pprint.pprint(dicts(nametree))
