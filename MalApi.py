#!/usr/bin/env python
# coding: utf-8

# In[125]:


import pandas as pd
import pandas as pd
from selenium import webdriver
import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep as sp

import warnings

#warnings.filterwarnings("ignore")

#=============================================================
# opening setion
 
driver = uc.Chrome()
driver.maximize_window()

#====================
# opening the url .

url = 'https://malapi.io/'
driver.get(url)

#======================
#export elements .

elements = driver.find_elements_by_css_selector("a[class = 'white-link map-item-link']")

#=========================
# initial lists.
links = []
names = []
dll   = []
doc = []
parameters = []
#==========================
#define the function .

def get_name_dll (lin):
    driver.get(lin)
    #print(link)
    sp(1)
    libs = driver.find_elements_by_css_selector("div[class = 'content']")
    sp(1)
    name = libs[0].text
    names.append(name)
    dll_name = libs[2].text
    dll.append(dll_name)
    sp(1)
    document = driver.find_element_by_class_name('link').text
    doc.append(document)

def extract_parameters (doc):
    for d in doc:
        try:
            driver.get(d)
            sp(1)
            p = driver.find_element_by_class_name('hljs-params').text.replace('\n' ,'' ).replace("[in]","").replace(" ","").replace("[out]","").replace("(","").replace("(","").replace(")","").lower()
            parameters.append(p)
        except:
            print(d)
            parameters.append("NaN")
            continue
    
#=====================

for i in range(len(elements)):
    link = elements[i].get_property('href')
    links.append(link)

for lin in links:
    get_name_dll(lin)
extract_parameters(doc)

sp(5)
from itertools import zip_longest
data = [dll , names , parameters]
exported = zip_longest(*data)
col = ["Dll_file" , "NAME","Parameters"]

df = pd.DataFrame(exported ,columns= col)
df2 = df.dropna(axis=0)

df2.to_csv("MalApi.csv")


# In[245]:





# In[ ]:




