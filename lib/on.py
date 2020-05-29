import requests
from bs4 import BeautifulSoup as bs
import re



def get_price():
    on1 = requests.get('https://miveplus.com/products/786').text
    #The god of replace :D
    parsed = str(bs(on1,'lxml').find_all('td')[1].find('strong')).replace('strong', '').replace('<>','').replace('</>','').replace(',','')
    return parsed
