# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 22:29:09 2018

@author: ASUS
"""

import requests
import json

url='https://woonzh.herokuapp.com/lazprice'

params={
    'product': 'mothball'
        }

jid=requests.get(url, params=params)
print(jid)

try:
    a=json.loads(jid.text)
    first=a['first']
    second=a['second']
except:
    t=1
#jid=jid.text
#
#params2={
#    'jobid': jid
#        }
#
#url2='https://woonzh.herokuapp.com/jobreport'
#report=requests.get(url2, params=params2)