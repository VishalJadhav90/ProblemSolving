import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup()
sess = requests.session()
r = sess.get("https://www.livemint.com/", verify=False)
soup = BeautifulSoup(r.text, 'html.parser')
for res in soup.find_all('a'):
    val = res.get('href')
    print(val)