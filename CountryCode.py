import requests
from bs4 import BeautifulSoup
import MySQLdb

conn = MySQLdb.connect(host="localhost",
                       user="root",
                       passwd="5328266",
                       db="wiki")
x = conn.cursor()

url = "https://countrycode.org/"
req = requests.get(url).text
soup = BeautifulSoup(req)
table = soup.find(class_='main-table')

for tr in table.find_all('tr')[1:]:
    col = tr.find_all('td')

    name = col[0].string.strip()
    iso_code = col[2].string.strip().split('/')
    iso = iso_code[0].strip()
    code = iso_code[1].strip()

    try:
        x.execute("""INSERT INTO countries (name,code, iso) VALUES (%s,%s,%s)""", (name, code,iso))
        conn.commit()
    except:
        conn.rollback()
    print(name)
    print(iso)
    print(code)
    print("---")