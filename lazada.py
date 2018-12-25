# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
import pandas as pd
import os

class lazadaCrawl:    
    def __init__(self, server=False, container = False, windows=True):
        self.xpaths={
            'name':'.//div[@class="c16H9d"]', 
            'price':'.//span[@class="c13VH6"]', 
            'orgPrice':'.//del[@class="c13VH6"]', 
            'discount':'.//span[@class="c1hkC1"]',
            'reviews': './/span[@class="c3XbGJ"]',
            'country': './/span[@class="c2i43- "]'}
        
        if server:
            t=1
        else:
            if container:
                self.chromepath='./chromedriver(linux)/chromedriver'
            
                self.options=webdriver.ChromeOptions()
                self.options.add_argument('--headless')
                self.options.add_argument('--no-sandbox')
                self.options.add_argument("--disable-setuid-sandbox")
                self.driver = webdriver.Chrome(chrome_options=self.options)
            else:
                if windows:
                    self.chromepath='chromedriver/chromedriver.exe'
                else:
                    self.chromepath='chromedriver(linux)/chromedriver'
                    
                self.options=webdriver.ChromeOptions()
                self.options.add_argument('--headless')
                self.driver = webdriver.Chrome(self.chromepath, chrome_options=self.options)                    
            
    def close(self):
        self.driver.quit()

    def parseData(self, info, attribute='innerText'):
        lst=[]
        for i in info:
            lst.append(i.get_attribute(attribute))
        
        return lst
    
    def getText(self, element, xpath):
        try:
            txt=element.find_element_by_xpath(xpath).text
        except:
            txt=''
        return txt
    
    def parseMain(self, info):
        df=pd.DataFrame(columns=['name', 'price', 'orginal price', 'discount', 'reviews', 'country'])
        count=0
        for i in info:
    #        print(i.text)
            lst=[]
            for j in self.xpaths:
                lst.append(self.getText(i, self.xpaths[j]))
            df.loc[count]=lst
            count+=1
        return df
    
    def nonServerGetProduct(self,name):
        self.driver.maximize_window()
        mainURL="https://www.lazada.sg"
        self.driver.get(mainURL)
        
        time.sleep(5)
        
#        first=self.driver.page_source
        
        inForm=self.driver.find_element_by_id('q')
        inForm.send_keys(name)
        
        button=self.driver.find_element_by_class_name('search-box__button--1oH7')
#        print(button)
        self.driver.execute_script("arguments[0].click();", button)
        
        time.sleep(4)
        
        mains=self.driver.find_elements_by_xpath('//div[@class="c3KeDq"]')
        
        df=self.parseMain(mains)
        
#        a={'first':first,
#           'second': self.driver.page_source}
        return df
    
    def getProduct(self,name):
    #    chromebin='/app/.apt/usr/bin/google-chrome'
    #    chromepath='/app/.chromedriver/bin/chromedriver' 
        GOOGLE_CHROME_BIN=os.getenv('GOOGLE_CHROME_BIN')
        CHROMEDRIVER_PATH=os.getenv('CHROMEDRIVER_PATH')
        
        print('google chrome bin: %s'%(GOOGLE_CHROME_BIN))
        print('chromdriver: %s'%(CHROMEDRIVER_PATH))
        
        options=Options()
        options.binary_location = GOOGLE_CHROME_BIN
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
    #    options.add_argument("user-data-dir=selenium") 
    #    options.add_argument('headless')
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
        driver.maximize_window()
        mainURL="https://www.lazada.sg"
    #    mainURL="https://blog.codeship.com/get-selenium-to-wait-for-page-load/"
        driver.get(mainURL)
        
        print(name)
        
        time.sleep(5)
        
        first=driver.page_source
        
        inForm=driver.find_element_by_id('q')
        inForm.send_keys(name)
        
        logo=driver.find_elements_by_class_name('lzd-logo-content')
        print('blogo %s'%(logo))
        
        driver.find_element_by_class_name('search-box__button--1oH7').click()
    ##    
        time.sleep(3)
    ##    
        logo=driver.find_elements_by_class_name('lzd-logo-content')
        print('blogo2 %s'%(logo))
    #    
        mains=driver.find_elements_by_xpath('//div[@class="c3KeDq"]')
        print(mains)
        df=self.parseMain(mains)
        print(len(df))
        a={'first':first,
           'second': driver.page_source}  
    
        time.sleep(1)
        
        driver.quit()
        
    #    df=pd.DataFrame(columns=['name', 'price', 'orginal price', 'discount', 'reviews', 'country'])
        return a
    
    def findAllHrefs(self):
        self.driver.maximize_window()
        mainURL="https://www.lazada.sg"
        self.driver.get(mainURL)
        classes=self.driver.find_elements_by_class_name('lzd-site-menu-sub')
        
        hrefStore=[]
        
        for element in classes:
            sub1=element.find_elements_by_class_name("sub-item-remove-arrow")
            print(len(list(sub1)))
            sub2=element.find_elements_by_class_name("lzd-site-menu-sub-item")
            print(len(list(sub2)))
            tem={}
            for i in sub1:
                name=i.find_element_by_xpath('.//span').get_attribute("innerHTML")
                tem[name]=i.find_element_by_xpath('.//a[@href]').get_attribute("href")
            for i in sub2:
                name=i.find_element_by_xpath('.//span').get_attribute("innerHTML")
                tem[name]=i.find_element_by_xpath('.//a[@href]').get_attribute("href")
            print(tem)
            hrefStore.append(tem)
        
        return hrefStore
    
    def crawlOneSubCat(self,url):
        self.driver.get(url)
        mains=self.driver.find_elements_by_xpath('//div[@class="c3KeDq"]')
        
        df=self.parseMain(mains)
        
        time.sleep(2)
        
        return df
    
    def crawlPopular(self):
        hrefs=self.findAllHrefs()
        
        dfCompile=[]
        
        for cat in hrefs:
            tem={}
            for subcat in cat:
                tem[subcat]=self.crawlOneSubCat(cat[subcat])
            dfCompile.append(tem)
        
        return dfCompile
    
#laz=lazadaCrawl()
#df=laz.nonServerGetProduct('nalgen water bottle')
#hrefs=laz.findAllHrefs()
#hrefs=laz.crawlPopular()
#time.sleep(5)
#df=laz.crawlOneSubCat(hrefs[0]['Action/Video Cameras'])
#laz.close()
