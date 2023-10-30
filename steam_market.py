from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import requests
import lxml
import os
import time

k=[]
v=[]
url="https://steamcommunity.com/market/search?q="
while True:
    item=input('Enter item: ')
    if len(item)<1:
        print("Try Again")
        continue
    elif item == 'done': break
    else:
        url=url+item
        response=requests.get(url)
        soup=BeautifulSoup(response.text,'lxml')
        
        names = soup.find_all('span', class_="market_listing_item_name") 
        for name in names:
            k.append(name.text)
        outer_span = soup.find_all('span', class_='market_table_value normal_price')
        for i in outer_span:
            prices = i.find_all('span', class_='normal_price')
            for price in prices:
                v.append(price.text)
        scrape=dict(zip(k,v))
        continue
print(scrape)

df = pd.DataFrame()
df['Name'] = scrape.keys()
df['Price'] = scrape.values()

writer = pd.ExcelWriter('scrape.xlsx', engine='openpyxl')
df.to_excel(writer, index=False)
writer._save()

def open_file(file_path):
    try:
        process = os.startfile(file_path)
        print(f"Opening {file_path}")
        return process
    except OSError as e:
        print(f"Error opening {file_path}: {e}")
        return None

file_path = 'Investment.xlsx'
a = open_file(file_path)
input('Press ENTER to exit') 