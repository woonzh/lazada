# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
import pandas as pd

xpaths={
    'name':'.//div[@class="c16H9d"]', 
    'price':'.//span[@class="c13VH6"]', 
    'orgPrice':'.//del[@class="c13VH6"]', 
    'discount':'.//span[@class="c1hkC1"]',
    'reviews': './/span[@class="c3XbGJ"]',
    'country': './/span[@class="c2i43- "]'}

def parseData(info, attribute='innerText'):
    lst=[]
    for i in info:
        lst.append(i.get_attribute(attribute))
    
    return lst

def getText(element, xpath):
#    print(xpath)
    try:
        txt=element.find_element_by_xpath(xpath).text
    except:
        txt=''
    return txt

def parseMain(info):
    df=pd.DataFrame(columns=['name', 'price', 'orginal price', 'discount', 'reviews', 'country'])
    count=0
    for i in info:
#        print(i.text)
        lst=[]
        for j in xpaths:
            lst.append(getText(i, xpaths[j]))
        df.loc[count]=lst
        count+=1
    return df

def nonServerGetProduct(name):
    chromepath='chromedriver\chromedriver.exe'
    
    options=webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(chromepath, chrome_options=options)
    driver.maximize_window()
    mainURL="https://www.lazada.sg"
    driver.get(mainURL)
    
    time.sleep(2)
    
    inForm=driver.find_element_by_id('q')
    inForm.send_keys(name)
    
    driver.find_element_by_class_name('search-box__button--1oH7').click()
    
    mains=driver.find_elements_by_xpath('//div[@class="c3KeDq"]')
    
    df=parseMain(mains)
    
    time.sleep(3)
    
    driver.quit()

    return df

def getProduct(name):
    chromebin='/app/.apt/usr/bin/google-chrome'
    chromepath='/app/.chromedriver/bin/chromedriver' 
    
    options=Options()
    options.binary_location = chromebin
    options.add_argument('--disable-gpu')
#    options.add_argument('--no-sandbox')
    options.add_argument('headless')
    driver = webdriver.Chrome(executable_path=chromepath, chrome_options=options)
    driver.maximize_window()
    mainURL="https://www.lazada.sg"
    driver.get(mainURL)
    
    time.sleep(2)
    
    inForm=driver.find_element_by_id('q')
    inForm.send_keys(name)
    
    driver.find_element_by_class_name('search-box__button--1oH7').click()
    
    mains=driver.find_elements_by_xpath('//div[@class="c3KeDq"]')
    
    df=parseMain(mains)
    print(len(df))
    
    time.sleep(3)
    
    driver.quit()

    return df