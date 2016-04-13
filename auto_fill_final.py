
# coding: utf-8

# In[4]:

import re
import sys
from robobrowser import RoboBrowser
from getpass import getpass

account = input('account:')
password = getpass('password:')

#use robobrowser module to manipulate web page 
browser = RoboBrowser(history = True)
browser.open('http://web1.cmu.edu.tw/stdinfo/login.asp')
form1 = browser.get_form(id = 'form1')
form1['f_id'].value = account
form1['f_pwd'].value = password
browser.submit_form(form1)

link_one = browser.get_link(text = '期中網路教學意見調查')
browser.follow_link(link_one)
list = []
for l in browser.get_links(text = re.compile('填寫')): 
    list.append(l)
list.pop(0)
for li in list:
    browser.follow_link(li)
    form2 = browser.get_form(id = 'thisform')
    form2['Cos_Q1'].value = '1'
    browser.submit_form(form2)
    

