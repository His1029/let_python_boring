from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("https://www.scskserviceware.co.jp/company/overview/")
data = html.read()
html = data.decode('utf-8')

# HTMLを解析
soup = BeautifulSoup(html, 'html.parser')

# 解析したHTMLから任意の部分のみを抽出（ここではtitleとbody）
title = soup.find("title")
body = soup.find("body")

print("title: " + title.text)
print("body: " + body.text)

title2 = soup.find("title").get_text()
body2 = soup.find("body").get_text()

print("title2: " + title2)
print("body2: " + body2)