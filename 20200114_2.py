# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:54:25 2019

@author: choeycui

For transforming coordinates from other CRS to Gaode CRS (GCJ-02) by calling Gaode API

"""

import pandas as pd
import requests as re
import socket

path = ''
out_path = ''
key = '' #高德API key
coord_old = 'gps' # 原始坐标系

x_col = 'X' # 代转经度列名
y_col = 'Y' # 代转纬度列名

x_new = 'lng_new' #转后经度列名
y_new = 'lat_new' #转后纬度列名

##############################################################################
url = 'https://restapi.amap.com/v3/assistant/coordinate/convert?'
params = {'locations':'',
          'coordsys':coord_old,
          'key':key}
lng_new = []
lat_new = []

b = open(path)
file_in = pd.read_csv(b)

coor_lng = file_in[x_col].apply(str)
coor_lat = file_in[y_col].apply(str)

locations = coor_lng + ',' + coor_lat    

for location in locations:
    params['locations'] = location
    response = re.get(url,params)
    lng_new.append(response.json()['locations'].split(',')[0])
    lat_new.append(response.json()['locations'].split(',')[1])
    
file_out = file_in

file_out[x_new] = lng_new
file_out[y_new] = lat_new

file_out.to_csv(out_path,index=False)
