import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url = 'https://www.jumia.co.ke/'

links = []
content = requests.get('https://www.jumia.co.ke/flash-sales/')
soup = BeautifulSoup(content.content, 'html.parser')


pageName = soup.find_all('article', class_='prd _fb _p col c-prd')


for item in pageName:
        for link in item.find_all('a', href=True):
            links.append(url + link['href'])

#testLink = 'https://www.jumia.co.ke/maybelline-new-york-superstay-skin-tint-shade-64-with-vitamin-c-191048304.html'
for link in links:
    content = requests.get(link)


soup = BeautifulSoup(content.content, 'html.parser')
productName = soup.find('h1', class_='-fs20 -pts -pbxs').text.strip()
#productBrand = soup.find('a', class_='_more').text.strip()
productPrice = soup.find('div', class_='-dif -i-ctr').text.strip()
#productDiscount = soup.find('span', '-b -ubpt -tal -fs24 -prxs').strip()
productRating = soup.find('div', class_='-df -i-ctr -pbs').text.strip()
try:
    productCount = soup.find('span', class_='-fsh0 -prs -fs12').text.strip()
except:
    productCount = 'no count'
item = {
    'content': content,
    'name': productName,
    'price': productPrice,
    #'discount': productDiscount,
    'rating': productRating,
    'count': productCount,
}

jumia = pd.read_csv('jumia_products.csv')
jumia.head(10)

























