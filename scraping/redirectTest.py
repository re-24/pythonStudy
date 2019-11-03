import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.chamanet.com/cgi/redirect.cgi', allow_redirects=False)
res.raise_for_status()
print(res.status_code)
print(res.history)