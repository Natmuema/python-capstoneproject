import requests
from bs4 import BeautifulSoup
import csv

# URL of the Jumia Kenya homepage
url = 'https://www.jumia.co.ke/'

# Check for the response and whether the site can be scraped.
def get_pagecontent(url):
    '''
    This helper function helps get the content from the site 
    and then gets to the required division so as to get the 
    required Jumia products.
    parameter:
      url (str): a string of the site you want to scrape
    returns:
      soup_content(bs4 object): from the required page
    '''
    response = requests.get(url)
    if response.status_code == 200:
        soup_content = BeautifulSoup(response.content, 'html.parser')
        return soup_content
    else:
        print("Failed to retrieve the page")
        return None

## Retrieve product name
def getproductname(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product name
    parameter:
      soup (bs4Object) : a BeautifulSoup object containing parsed HTML
    returns:
      product_name (list) : list of product names
    '''
    product_name = [item.text.strip() for item in soup.select('h1', class_='-fs20 -pts -pbxs')]
    return product_name

## Retrieve Brand Name
def getproductbrand(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product brand
    parameter:
      soup (bs4Object) : a BeautifulSoup object containing parsed HTML
    returns:
      product_brand (list) : list of product brands
    '''
    product_brand = [item.text.strip() for item in soup.select('div.info > div.brand')]
    return product_brand

## Retrieve Price
def getproductprice(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product price
    parameter:
      soup (bs4Object) : a BeautifulSoup object containing parsed HTML
    returns:
      product_price (list) : list of product prices
    '''
    product_price = [item.text.strip() for item in soup.select('div.info > div.price')]
    return product_price

## Retrieve the Discount
def getproductdiscount(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product discount
    parameter:
      soup (bs4Object) : a BeautifulSoup object containing parsed HTML
    returns:
      product_discount (list) : list of product discounts
    '''
    product_discount = [item.text.strip() for item in soup.select('div.info > div.discount')]
    return product_discount

## Retrieve the Number of reviews.
def getproductreviewcnt(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product reviews
    parameter:
      soup (bs4Object) : a BeautifulSoup object containing parsed HTML
    returns:
      product_reviews (list) : list of product reviews
    '''
    product_reviewcnt = [item.text.strip() for item in soup.select('div.info > div.reviews')]
    return product_reviewcnt

## Retrieve the ratings.
def getproductrating(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract product rating
    parameter:
      soup (bs4Object) : a BeautifulSoup object containing parsed HTML
    returns:
      product_rating (list) : list of product ratings
    '''
    product_rating = [item.text.strip() for item in soup.select('div.info > div.rating')]
    return product_rating

## Retrieve the remaining stock.
def getproductcount(soup):
    '''
    Helper function uses the soup object obtained from the product page
    and then extract remaining product stock
    parameter:
      soup (bs4Object) : a BeautifulSoup object containing parsed HTML
    returns:
      product_count (list) : list of product items remaining in stock
    '''
    product_count = [item.text.strip() for item in soup.select('div.info > div.stock')]
    return product_count

## Determine the actual customer satisfaction rating.
def getactualrating(reviews, rating):
    '''
    Helper function uses the review and rating columns obtained from the created dataframe
    and then calculate the final actual rating.
    parameter:
      reviews (list) : list of product reviews
      rating (list) : list of product ratings
    returns:
      actual_rating (list) : list of actual ratings calculated
    '''
    actual_rating = [(float(rat.split()[0]) / 5.0) * 100 for rat in rating]
    return actual_rating

# Calling out the functions and creating a list of lists containing the data
soup = get_pagecontent(url)
if soup:
    name = getproductname(soup)
    brand = getproductbrand(soup)
    price = getproductprice(soup)
    discount = getproductdiscount(soup)
    review = getproductreviewcnt(soup)
    rating = getproductrating(soup)

    list_of_lists = [name, brand, price, discount, review, rating]

    # Save and review the product data
    with open('jumia_products.csv', 'w') as jumia_file:
        fieldnames = ["name", "brand", "price", "discount", "reviews", "rating"]
        
        csvwriter = csv.writer(jumia_file)
        csvwriter.writerow(fieldnames)
        
        # Loop through product list to update csv file
        for i in range(len(name)):
            product = [list_of_lists[j][i] for j in range(len(list_of_lists))]
            csvwriter.writerow(product)
            
        print("Done! All products have been added to CSV file")









