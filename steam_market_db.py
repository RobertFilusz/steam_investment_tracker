from bs4 import BeautifulSoup
import pandas as pd
import requests
import lxml
import sqlite3

conn=sqlite3.connect('scrape.sqlite')
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS Invest')
cur.execute('CREATE TABLE Invest (name TEXT, price INTEGER)')
response=requests.get("https://steamcommunity.com/market/search?q=paris+2023+capsule") #will probably change to user input in future, for now am only interested in specific items
soup=BeautifulSoup(response.text,'lxml')


items = soup.find_all('a', class_='market_listing_row_link')
for element in items:
    #names=soup.find(class_="market_listing_item_name") ||| for some reason prints the same item multiple times instead of multiple items once
    pieces=element.text.split()
    name=pieces[7]+" "+pieces[8]+" "+pieces[9]+" "+pieces[10]+" "+pieces[11]
    price=pieces[3]
    cur.execute('SELECT price FROM Invest WHERE name=?',(name,))
    row=cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Invest (name, price) VALUES (?, ?)''',(name,price))
    conn.commit()

sqlstr='SELECT name, price FROM Invest ORDER BY price DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])

cur.close()