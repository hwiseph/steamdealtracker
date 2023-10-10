import requests
from bs4 import BeautifulSoup
import csv

# Define the SteamDB Deals URL
steamdb_deals_url = 'https://steamdb.info/sales/'

# Send an HTTP GET request to the SteamDB Deals page
response = requests.get(steamdb_deals_url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all deal rows in the table
deal_rows = soup.find_all('tr', class_='app')

# Create a list to store deal information
deals = []

for row in deal_rows:
    # Extract information like title, price, discount, and rating
    title = row.find('td', class_='app-name').text.strip()
    price = row.find('td', class_='app-price').text.strip()
    discount = row.find('td', class_='app-discount').text.strip()
    
    # Some games may not have ratings, so use a try-except block
    try:
        rating = float(row.find('td', class_='app-rating').text.strip())
    except ValueError:
        rating = 0.0  # Set an arbitrary low rating for games without ratings
    
    # Append the deal information to the list
    deals.append({'title': title, 'price': price, 'discount': discount, 'rating': rating})

# Sort the deals by rating in descending order
deals.sort(key=lambda x: x['rating'], reverse=True)

# Specify the CSV file name
csv_file_name = 'top_20_steam_deals.csv'

# Write the top 20 deals to a CSV file
with open(csv_file_name, 'w', newline='') as csvfile:
    fieldnames = ['Title', 'Price', 'Discount', 'Rating']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()
    
    # Write the top 20 deals
    for deal in deals[:20]:
        writer.writerow({'Title': deal['title'], 'Price': deal['price'], 'Discount': deal['discount'], 'Rating': deal['rating']})

print(f'Top 20 deals based on rating have been saved to {csv_file_name}.')