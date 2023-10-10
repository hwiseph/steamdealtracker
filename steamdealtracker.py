import requests
from bs4 import BeautifulSoup

steamdb_deal_url = 'https://steamdb.info/sales/'

resposne = requests.get(steamdb_deals_url)

soup = BeautifulSoup(response.content, 'html.parser')

# Find all deal rows in the table
deal_rows = soup.find_all('tr', class_='app')

 # Extract information like title, price, and discount
for row in deal_rows:
    title = row.find('td', class_='app-name').text.strip()
    price = row.find('td', class_='app-price').text.strip()
    discount = row.find('td', class_='app-discount').text.strip()

    # Print the information
    print(f'Title: {title}')
    print(f'Price: {price}')
    print(f'Discount: {discount}')
    print()