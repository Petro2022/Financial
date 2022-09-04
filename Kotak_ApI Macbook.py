#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install -e "git+https://github.com/paramatrixtech/ksapi.git#egg=ks_api_client&subdirectory=./python"


# In[2]:


python setup.py install --user


# In[3]:


pip install setuptools


# In[1]:


access_token="b75bed29-5f91-3fce-87cd-fbf8c7742569"
consumer_key = "9ibDy_ved1fzV7MHYIJmpDFFYsUa"
consumer_secret = "raxkZMTEzY4aszsUqIqWSl3otkga"

userid = "ANI563"


# In[2]:


from ks_api_client import ks_api
# Defining the host is optional and defaults to https://sbx.kotaksecurities.com/apim
# See configuration.py for a list of all supported configuration parameters.
client = ks_api.KSTradeApi(access_token = "b75bed29-5f91-3fce-87cd-fbf8c7742569", userid = "ANI563", consumer_key = "9ibDy_ved1fzV7MHYIJmpDFFYsUa",ip = "127.0.0.1", app_id = "test",                         host = "https://tradeapi.kotaksecurities.com/apim", consumer_secret = "raxkZMTEzY4aszsUqIqWSl3otkga")


# In[3]:


client


# In[5]:


client.login(password = "Kotak@123")
client.session_2fa(access_code = "2902")


# In[24]:


pip install requests


# In[7]:


url='https://tradeapi.kotaksecurities.com/apim/scripmaster/1.1/filename'


# In[8]:


import requests
headers= {'accept':'application/json',"consumerKey":"9ibDy_ved1fzV7MHYIJmpDFFYsUa","Authorization":"Bearer b75bed29-5f91-3fce-87cd-fbf8c7742569"}
res=requests.get(url, headers=headers).json()
res


# In[9]:


fnourl=res['Success']['fno']
print(fnourl)


# In[10]:


import pandas as pd
fnodf=pd.read_csv(fnourl,sep='|')


# In[9]:


fnodf.head()


# In[22]:


fnodf['segment'].unique()


# In[14]:


NIFTY=fnodf[(fnodf['instrumentName']=='NIFTY') & (fnodf['segment']=='FO') &(fnodf['expiry']=='28JUL22') &(fnodf['instrumentType']=='FI')]
NIFTY


# In[ ]:





# In[28]:


NIFTY['instrumentType'].unique()


# In[31]:


client.session_token


# In[15]:


import requests
url2='https://tradeapi.kotaksecurities.com/apim/margin/1.0/margin'
headers= {'accept':'application/json',"consumerKey":"9ibDy_ved1fzV7MHYIJmpDFFYsUa",'sessionToken':client.session_token,"Authorization":"Bearer b75bed29-5f91-3fce-87cd-fbf8c7742569"}
margin=requests.get(url2, headers=headers).json()
margin


# In[28]:


orders=client.place_order(order_type = "N", instrument_token = 1407, transaction_type = "BUY",                   quantity = 1, price = 300, disclosed_quantity = 0, trigger_price = 0,                   tag = "string", validity = "GFD", variety = "REGULAR")


# In[11]:


client.quote(instrument_token = 480)


# In[24]:


import requests
url3='https://tradeapi.kotaksecurities.com/apim/quotes/v1.0/instruments/12162'

headers= {'accept':'application/json',"consumerKey":"9ibDy_ved1fzV7MHYIJmpDFFYsUa",'sessionToken':client.session_token,"Authorization":"Bearer b75bed29-5f91-3fce-87cd-fbf8c7742569"}
quotes=requests.get(url3, headers=headers).json()
quotes


# In[25]:


ltp=float(quotes['success'][0]['ltp'])
nearest_atm=round(ltp//100)*100
nearest_atm


# In[26]:


NIFTY=fnodf[(fnodf['instrumentName']=='NIFTY') & (fnodf['segment']=='FO') &(fnodf['expiry']=='28JUL22') &(fnodf['instrumentType']=='OI')&(fnodf['strike']==nearest_atm)]
NIFTY


# In[ ]:




