import requests
import json

import sys
sys.path.insert(0,'bs4.zip')
from bs4 import BeautifulSoup

#Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}


def compare_prices(product_laughs,product_glomark):
    #TODO: Aquire the web pages which contain product Price
    html_content_laughs = requests.get(product_laughs)
    html_content_glomark = requests.get(product_glomark)
    
    
    #TODO: LaughsSuper supermarket website provides the price in a span text.
    soup_laughs = BeautifulSoup(html_content_laughs.content, 'html.parser')
    soup_glomark = BeautifulSoup(html_content_glomark.content, 'html.parser')


    
    price_text_laughs = soup_laughs.find("span",{"class":"regular-price"}).text.strip()[3:]
    price_laughs = float(price_text_laughs)
    glomark_script= soup_glomark.find('script',{"type":"application/ld+json"}).text
    glomark_data=json.loads(glomark_script)
    price_glomark = float(glomark_data['offers'][0]['price'])
    
    product_name_laughs=soup_laughs.find(class_="product-name").get_text()
    product_name_glomark=soup_glomark.find(class_="product-title").find('h1').get_text()

    #TODO: Glomark supermarket website provides the data in jason format in an inline script.
    #You can use the json module to extract only the price
    
    
    #TODO: Parse the values as floats, and print them.
    
    print('Laughs  ',product_name_laughs,'Rs.: ' , price_laughs)
    print('Glomark ',product_name_glomark,'Rs.: ' , price_glomark)
    
    if(price_laughs>price_glomark):
        print('Glomark is cheaper Rs.:',price_laughs - price_glomark)
    elif(price_laughs<price_glomark):
        print('Laughs is cheaper Rs.:',price_glomark - price_laughs)    
    else:
        print('Price is the same')


compare_prices('https://scrape-sm1.github.io/site1/COCONUT%20market1super.html','https://glomark.lk/coconut/p/11624');