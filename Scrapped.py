import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='log/scraping.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# URL of the Sigma-Aldrich website
url = 'https://www.sigmaaldrich.com/IN/en'

# Send a GET request to the URL
print(f"Sending GET request to URL: {url}")
logging.info(f"Sending GET request to URL: {url}")
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print('Webpage retrieval successful')
    logging.info('Webpage retrieval successful')

    # Parse the HTML content of the webpage
    print('Parsing HTML content...')
    logging.info('Parsing HTML content...')
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the product names and their respective URLs
    product_boxes = soup.find_all('div', class_='product-box')

    # Create lists to store product names and URLs
    product_names = []
    product_urls = []

    # Loop through each product box and extract its name and URL
    for box in product_boxes:
        product_link = box.find('a', class_='product-box__name-link')
        if product_link:
            product_names.append(product_link.text.strip())
            product_urls.append(url + product_link['href'])

    print(f"Found {len(product_names)} products on the webpage")
    logging.info(f"Found {len(product_names)} products on the webpage")

    # Create a DataFrame to store the data
    df = pd.DataFrame({'Product Name': product_names, 'URL': product_urls})

    # Export the DataFrame to an Excel file
    print('Exporting data to Excel file...')
    logging.info('Exporting data to Excel file...')
    df.to_excel('sigma_aldrich_products.xlsx', index=False)

    print('Data saved successfully in sigma_aldrich_products.xlsx')
    logging.info('Data saved successfully in sigma_aldrich_products.xlsx')
else:
    print('Failed to retrieve the webpage.')
    logging.error('Failed to retrieve the webpage.')
