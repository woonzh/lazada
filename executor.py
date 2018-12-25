# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 22:06:05 2018

@author: ASUS
"""

import pandas as pd
from lazada2 import lazada

def getProduct(names, dataType='dataframe'):
    lazCrawler=lazada()
    df=lazCrawler.nonServerGetProduct(names, dataType)
    lazCrawler.close()
    return df
    
#df=getProduct(['huawei mate 20 pro'], 'json')
    