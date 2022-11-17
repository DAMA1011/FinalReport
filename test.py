import requests as req
from bs4 import BeautifulSoup as bs

url = "https://zip5.5432.tw/cityzip/%E8%87%BA%E5%8C%97%E5%B8%82/%E6%9D%BE%E5%B1%B1%E5%8D%80"

res = req.get(url)
res.encoding="utf-8"
soup = bs(res.text,"lxml")

road = soup.select("td.zip-road a")

for a in road:
    with open("松山區路名.txt","a",encoding="utf-8") as f:
        f.write(f'"{a.get_text()}",')
        print(a.get_text())