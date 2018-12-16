# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 22:29:09 2018

@author: ASUS
"""

import requests
import json

url='https://woonzh.herokuapp.com/lazprice'

url='http://localhost:8080/local'

params={
    'product': 'fossil watch'
        }

jid=requests.get(url, params=params)
print(jid)
a=jid.text

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