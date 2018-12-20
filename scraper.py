# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 21:59:54 2018

@author: ASUS
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
import pandas as pd
import os
import random

class wait_for_page_load(object):
    def __init__(self, browser, minTime=1, maxTime=3):
        self.browser = browser
        self.minTime=minTime
        self.maxTime=maxTime

    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')

    def page_has_loaded(self):
        new_page = self.browser.find_element_by_tag_name('html')
        return new_page.id != self.old_page.id
    
    def randomSleep(self):
        sleeptime=random.uniform(self.minTime, self.maxTime)
        time.sleep(sleeptime)
        
    def randomScroll(self):
        t=1

    def wait_for(self,condition_function):
        start_time = time.time() 
        while time.time() < start_time + 5: 
            if condition_function():
                self.randomSleep()
                return True 
            else: 
                time.sleep(0.2)
        raise Exception('Timeout waiting for {}'.format('loading'))

    def __exit__(self, *_):
        self.wait_for(self.page_has_loaded)

class scraper:
    def __init__(self, server=False, container = False, windows=True):
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
                self.driver.maximize_window()
            else:
                if windows:
                    self.chromepath='chromedriver/chromedriver.exe'
                else:
                    self.chromepath='chromedriver(linux)/chromedriver'
                    
                self.options=webdriver.ChromeOptions()
#                self.options.add_argument('--headless')
                self.driver = webdriver.Chrome(self.chromepath, chrome_options=self.options)
                self.driver.maximize_window()
        
    def pageLoad(self, url, minWait=1, maxWait=5):
        with wait_for_page_load(self.driver):
            self.driver.get(url)
    
    def click(self, iden, inVal, butClass):
        with wait_for_page_load(self.driver):
            inForm=self.driver.find_element_by_id(iden)
            inForm.send_keys(inVal)
            button=self.driver.find_element_by_class_name(butClass)
            self.driver.execute_script("arguments[0].click();", button)
                
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
    
    def parseMain(self, columns, xpaths):
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