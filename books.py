import requests
from bs4 import BeautifulSoup
base_url="https://books.toscrape.com/"
html=requests.get(base_url).text
data=BeautifulSoup(html,"html.parser")
books_data=data.select('article.product_pod h3 a')
price_tag=data.select('article.product_pod p.price_color')
#print(books_name)
#print(price_tag)

for books_title in books_data:
    print(books_title['title'])

for tag in price_tag:
    price_text= tag.get_text()
    print(price_text)