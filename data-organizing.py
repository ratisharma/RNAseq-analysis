#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:17:18 2017

@author: ratisharma
"""

import pandas as pd

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
    
df1 = pd.read_csv('geneNames-CDS.csv')
print(df1.head())
#df1.dropna(axis=0)
print(df1.tail())

