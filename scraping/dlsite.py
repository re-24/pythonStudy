import requests
from requests.adapters import HTTPAdapter
import webbrowser
from bs4 import BeautifulSoup

#: :type: requests
session = requests.session()
url = 'https://dlsite.com/pro'
res = session.get(url)

print(res.text)
