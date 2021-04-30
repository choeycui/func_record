# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 16:57:44 2021

@author: cuch9001
"""

import geopandas as gpd
from xyconvert import wgs2gcj
import numpy as np
from shapely.geometry import mapping, shape, MultiPolygon

def coord_trans(geom):
    if geom.geom_type == 'MultiPolygon':
        return MultiPolygon([coord_trans(i) for i in geom.geoms])
    if geom.geom_type == 'Polygon':
        geojson = mapping(geom)
        geojson['coordinates'] = tuple([tuple(map(tuple, wgs2gcj(np.array(geojson['coordinates'][0])))),])
        return shape(geojson)

test = gpd.read_file('C:/Users/cuch9001/Desktop/行政边界/C11_3_region_GCJ02.shp').to_crs('epsg:4030')

test1 = test.copy()

test1['geometry'] = test1['geometry'].apply(lambda x: coord_trans(x))

mapping(test['geometry'][66])['coordinates'][0][0][0]
mapping(test1['geometry'][66])['coordinates'][0][0][0]
