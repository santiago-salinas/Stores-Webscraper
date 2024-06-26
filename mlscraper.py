# -*- coding: utf-8 -*-
"""MLScraper.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h9xdXoE3agLDyBCEBYuQFID5l93KlPNP
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://listado.mercadolibre.com.uy/vinilo-pizarra#D[A:vinilo%20pizarra,L:undefined]"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find all span elements with the specific class
spans = soup.find_all("span", class_="andes-money-amount__fraction", attrs={"aria-hidden": "true"})

# Extract and print the text from each span
for span in spans:
    print(span.text)

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://listado.mercadolibre.com.mx/plush-toy-fisher-price-smart-puppy-learn-for-6-36-months#D[A:Plush%20Toy%20Fisher-Price%20Smart%20Puppy%20Learn%20for%206-36%20Months]"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find all items
items = soup.find_all("div", class_="ui-search-result__content-wrapper")

# Extract and print the price, name, and URL for each item
for item in items:
    # Extract the name
    name_tag = item.find("h2", class_="ui-search-item__title")
    if name_tag:
        name = name_tag.text
    else:
        name = "N/A"

    # Extract the price
    price_tag = item.find("span", class_="andes-money-amount__fraction", attrs={"aria-hidden": "true"})
    if price_tag:
        price = price_tag.text
    else:
        price = "N/A"

    # Extract the URL
    url_tag = item.find("a", class_="ui-search-item__group__element ui-search-link__title-card ui-search-link")
    if url_tag and 'href' in url_tag.attrs:
        item_url = url_tag['href']
    else:
        item_url = "N/A"

    print(f"Name: {name}")
    print(f"Price: {price}")
    print(f"URL: {item_url}")
    print("-------------")