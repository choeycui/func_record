# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 12:14:31 2020

@author: choeycui

"""

import geopandas as gpd
import pandas as pd

def overlap_detect(df, shape_id='id',crs_output='epsg:4030'):
#
# This is the function to detect all the overlaps within a shapefile.
# ID in both sides are saved
#
    shapes = []
    for i in range(0, df.shape[0]):
        if i < df.shape[0]:
            alternate = df[(df['geometry'].intersects(df.iloc[i]['geometry'])) & (~df['geometry'].touches(df.iloc[i]['geometry']))].iloc[i+1:]
            alternate.reset_index(drop=True,inplace=True)
            for j in range(0,alternate.shape[0]):
                inter_buffer = df.iloc[i]['geometry'].intersection(alternate.iloc[j]['geometry'])
                if not inter_buffer.is_empty:
                    print(str(i) + str(j))
                    shapes.append([df.iloc[i][shape_id],alternate.iloc[j][shape_id],inter_buffer])
                    print('shape cnt: ' + str(len(shapes)))
    results = gpd.GeoDataFrame(pd.DataFrame(shapes,columns=[shape_id + '_x', shape_id + '_y','geometry']),crs=crs_output,geometry = 'geometry')
    return results

def pnt_count(df_points, df_polygons, bound_cnt = False, poly_id='block_id'):
#
# This function is used to count points intersect or within polygons
# bound_cnt: if True, points on boundary are counted
# pnt_id: column name of unique points' id
# poly_id: column name of polygons' id
#
# This function returns a polygons geodataframe based on df_polygon, count result added to column
    if bound_cnt:
        pnt_poly = gpd.sjoin(df_points, df_polygons, how='left', op='intersects')
    else:
        pnt_poly = gpd.sjoin(df_points, df_polygons, how='left', op='within')
    pivot = pd.pivot_table(pnt_poly,values=[df_points.columns[0]],index=[poly_id],aggfunc='count',dropna=False).reset_index()
    polygon_new = pd.merge(df_polygons,pivot,how='left',left_on=[poly_id],right_on=[poly_id])
    polygon_new.rename(columns={df_points.columns[0]:'NUMPOINTS'},inplace=True)
    polygon_new['NUMPOINTS'].fillna(0,inplace=True)
    return polygon_new
