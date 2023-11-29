from bs4 import BeautifulSoup
import pandas as pd
import requests
import lxml
import psycopg2
import sys

try:
    conn = psycopg2.connect(
        user="postgres",
        password="p4$S(postgres)W0r|)",
        host="127.0.0.1",
        port=5432,
        database="investment",
    )
except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL Platform: {e}")
    sys.exit(1)
cur = conn.cursor()
cur.execute("DROP DATABASE IF EXISTS investment")
cur.execute("CREATE DATABASE investment")
cur.execute("DROP TABLE IF EXISTS investments")
cur.execute("CREATE TABLE investments (name TEXT, price TEXT)")

response = requests.get("https://steamcommunity.com/market/search?q=paris+2023+capsule")
soup = BeautifulSoup(response.text, "lxml")


items = soup.find_all("a", class_="market_listing_row_link")
for element in items:
    # names=soup.find(class_="market_listing_item_name") ||| for some reason prints the same item multiple times instead of multiple items once
    pieces = element.text.split()
    name = (
        pieces[7]
        + " "
        + pieces[8]
        + " "
        + pieces[9]
        + " "
        + pieces[10]
        + " "
        + pieces[11]
    )
    price = pieces[3]
    cur.execute("SELECT price FROM investments WHERE name=%s", (name,))
    row = cur.fetchone()
    if row is None:
        cur.execute(
            """INSERT INTO investments (name, price) VALUES (%s, %s)""", (name, price)
        )
    conn.commit()

cur.execute("SELECT name, price FROM Investments ORDER BY price DESC LIMIT 10")
for row in cur.fetchall():
    print(row)

cur.close()
conn.close()
