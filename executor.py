# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 22:06:05 2018

@author: ASUS
"""

import pandas as pd
from lazada2 import lazada

def getProduct(names, dataType='dataframe'):
    lazCrawler=lazada()
    print('test')
    df=lazCrawler.nonServerGetProduct(names, dataType)
    print('test2')
    lazCrawler.close()
    return df

def getHrefs(dataType='dataframe'):
    lazCrawler=lazada()
    hrefs=lazCrawler.findAllHrefs(dataType)
    lazCrawler.close()
    return hrefs

def getSubCat(url):
    lazCrawler=lazada()
    df=lazCrawler.crawlOneSubCat(url, 'dataframe')
    lazCrawler.close()
    return df
    
#df=getProduct(['huawei mate 20 pro'], 'json')
    