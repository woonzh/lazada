# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 22:29:09 2018

@author: ASUS
"""

import requests

url='https://woonzh.herokuapp.com/lazprice'

params={
    'product': 'plastic containers'
        }

jid=requests.get(url, params=params)
#jid=jid.text
#
#params2={
#    'jobid': jid
#        }
#
#url2='https://woonzh.herokuapp.com/jobreport'
#report=requests.get(url2, params=params2)