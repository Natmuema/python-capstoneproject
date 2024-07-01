import requests
from bs4 import BeautifulSoup
import csv

# URL of the Jumia Kenya homepage
url = 'https://www.jumia.co.ke/'

#  check for the response and whether the site can be scrapped.
response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve the webpage")
    exit()

# Parse the page content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the "Deals orf the Week" section
deals_section = soup.find('section', {'class': 'card -oh _fw -rad4'})

# Ensure we have found the deals section
if not deals_section:
    print("Deals of the Week section not found")
    exit()

# Find all product links in the "Deals of the Week" section
product_cards = deals_section.find_all('article', {'class': 'prd'})

# Function to extract product details
def get_product_details(product_card):
    try:
        product_name = product_card.find('a', {'class': 'link'}).get('title')
    except AttributeError:
        product_name = None

    try:
        brand_name = product_card.find('a', {'class': 'brand'}).text.strip()
    except AttributeError:
        brand_name = None

    try:
        price = product_card.find('div', {'class': 'prc'}).text.strip().replace('KSh ', '').replace(',', '')
    except AttributeError:
        price = None

    try:
        discount = product_card.find('div', {'class': 'bdg _dsct'}).text.strip().replace('-', '').replace('%', '')
    except AttributeError:
        discount = None

    try:
        reviews = product_card.find('div', {'class': 'rev'}).text.strip()
        reviews = re.findall(r'\d+', reviews)[0]  # Extract the number from text like "20 reviews"
    except AttributeError:
        reviews = 0

    try:
        rating = product_card.find('div', {'class': 'stars _s'}).get('style')
        rating = re.findall(r'\d+', rating)[0]  # Extract the number from style like "width: 80%"
        rating = float(rating) / 20  # Convert width percentage to rating out of 5
    except AttributeError:
        rating = None

    return {
        'Product Name': product_name,
        'Brand Name': brand_name,
        'Price (Ksh)': price,
        'Discount (%)': discount,
        'Total Number of Reviews': reviews,
        'Product Rating (out of 5)': rating,
    }

# Extract details for each product
products = []
for card in product_cards:
    product_details = get_product_details(card)
    products.append(product_details)

# Save to a CSV file
csv_file = 'jumia_deals_of_the_week.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=products[0].keys())
    writer.writeheader()
    writer.writerows(products)

print(f"Data saved to {csv_file}")


