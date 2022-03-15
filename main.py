import requests
from bs4 import BeautifulSoup
import urllib.request

URL = 'https://www.newyorker.com/magazine'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/99.0.4844.51 Safari/537.36', 'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('img')

    for item in items:
        name = item.get('src')
        img_data = requests.get(name).content
        name = name.replace(":", "").replace("/", "")
        with open(name, 'wb') as handler:
            handler.write(img_data)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print("Error")


parse()
