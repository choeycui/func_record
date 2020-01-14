# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:16:27 2020

@author: cuch9001
"""

import requests
import pandas as pd

# Return the locate coordinates and accuracy by input the address and city
# Enter your Gaode API key behind ak
def address(address,city,INFO=['location'],ak=''):
    result = {}
    url="https://restapi.amap.com/v3/geocode/geo?key=%s&address=%s&city=%s"%(ak,address,city)
    data=requests.get(url)
    contest=data.json()
    for key in INFO:
        result[key] = contest['geocodes'][0][key]
    return  result

def location_append(df, addr, city, level=True):
    if level:
        COL = ['location','level']
    else:
        COL = ['location']
    coord = pd.DataFrame(columns = [addr,city] + COL)
    add = dict(zip(list(df[addr]),list(df[city])))
    cnt = 0
    for key,value in add.items():
        try:
                coord = coord.append([{**{addr:key,city:value},**address(key,value,INFO=COL)}],ignore_index=True)
        except:
                coord = coord.append([{**{addr:key,city:value},**dict(zip(COL,['None']*len(COL)))}],ignore_index=True)
        cnt += 1
        print(cnt)
    coord['lon'] = coord['location'].apply(lambda x : x.split(',')[0])
    coord['lat'] = coord['location'].apply(lambda x : x.split(',')[-1])
    df_new = pd.merge(df,coord,how='left',left_on=[addr,city],right_on=[addr,city])
    return df_new
