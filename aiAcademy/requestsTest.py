from bs4 import BeautifulSoup
import requests

html = requests.get("https://aiacademy.jp/gym/").text

# HTMLを解析
soup = BeautifulSoup(html, 'html.parser')

data = soup.select('body > div > section.p-top-firstView > div.p-top-firstView__wrap > div > div > h2 >h2 ')
print(data)
