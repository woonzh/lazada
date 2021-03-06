# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 01:00:19 2018

@author: ASUS
"""

from scraper import scraper
import time
import pandas as pd

class lazada(scraper):
    def __init__(self):
        scraper.__init__(self, windows=False, container=True)
        self.prodxpaths={
            './/div[@class="c16H9d"]':'innerText', 
            './/span[@class="c13VH6"]':'innerText', 
            './/del[@class="c13VH6"]':'innerText', 
            './/span[@class="c1hkC1"]':'innerText',
            './/span[@class="c3XbGJ"]':'innerText',
            './/span[@class="c2i43- "]':'innerText',
            './/div[@class="c16H9d"]//a[@href]':'href'}
        self.columns=['name', 'price', 'original price', 'discount', 'reviews', 'country', 'href']
        self.mainURL="https://www.lazada.sg"
        self.hrefxpaths={
            './/span':"innerHTML",
            './/a[@href]':'href',
            '':'data-cate'
                }
        self.mainCatxpaths={
            './/span':'innerHTML',
            '':'id'
                }
        self.mainCatColumns=['name', 'id']

    def nonServerGetProduct(self,names, dataType='dataframe'):
        self.pageLoad(self.mainURL)
        
        lst={}
        
        for name in names:
            self.click('q', name, 'search-box__button--1oH7')
            df= self.parseMain(self.columns, '//div[@class="c3KeDq"]', self.prodxpaths, self.driver, dataType)
            lst[name]=df
               
        return lst
    
    def findAllHrefs(self, dataType='dataframe'):
        self.pageLoad(self.mainURL)
        
        columns=['name', 'href', 'cate']
#        main=[]
        
#        classes=self.driver.find_elements_by_class_name('lzd-site-menu-sub')
        
        df1=self.parseMain(columns, '//li[@class="sub-item-remove-arrow"]', self.hrefxpaths, self.driver, dataType)
        df2=self.parseMain(columns, '//li[@class="lzd-site-menu-sub-item"]', self.hrefxpaths, self.driver, dataType)
        df=df1+df2
        
        mainCat=self.parseMain(self.mainCatColumns, '//li[@class="lzd-site-menu-root-item"]', self.mainCatxpaths, self.driver, dataType)
        
        for i in mainCat:
            i['subcats']=[]
        
                
        for i in df:
            category=int(i['cate'].split('_')[1])-1
            mainCat[category]['subcats'].append(i)
        
        return mainCat
        if dataType=='dataframe':
            return df1.append(df2)
        if dataType=='json':
            return mainCat
    
    def crawlOneSubCat(self,url, dataType):
        self.pageLoad(url)        
        df=self.parseMain(self.columns, '//div[@class="c3KeDq"]', self.prodxpaths, self.driver, dataType)
        
        return df
    
    def crawlPopular(self):
        hrefs=self.findAllHrefs()
        
        dfCompile={}
        
        for i in range(len(hrefs)):
            dfCompile[hrefs.iloc[i,0]]=self.crawlOneSubCat(hrefs.iloc[i, 1])
        
        return dfCompile
    
#laz=lazada()
#mainCat=laz.findAllHrefs('json')

#df=laz.nonServerGetProduct(['addidas bag'], 'json')

#laz.close()