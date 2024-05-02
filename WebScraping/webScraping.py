import requests 
from bs4 import BeautifulSoup

url='https://www.ndtv.com/'

page = requests.get(url)
print(page)
soup = BeautifulSoup(page.text, "html.parser")
proftags = soup.findAll()
print(proftags)
proftags = soup.select('title')
print(proftags)
final = proftags[0].getText()
print(final)