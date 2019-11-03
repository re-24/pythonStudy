import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

session = requests.session()

USER = 're-24'
PASS = 'raiki777'


url_login = "https://qiita.com/login"
res = session.get(url_login)
token = BeautifulSoup(res.text, 'html.parser').select('body > div.sessionsLayout > div > div > div > div.row > div.col-sm-6.sessionsLayoutFormColumn > form > input[type=hidden]:nth-child(2)')

login_info = {
    "identity": USER,
    "password": PASS,
    "authenticity_token": token[0].attrs['value']
}

res = session.post(url_login, data=login_info)
bs = BeautifulSoup(res.text, 'html.parser')
for a in bs.select('a'):
    print(a['href'])