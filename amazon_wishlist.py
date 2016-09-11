from urllib.parse import urlparse
from bs4 import BeautifulSoup
import sys
import requests
import re

def print_error_msg(msg):
    print(msg)
    sys.exit(1)

def find_total_price():
    if len(sys.argv) == 2:
        url = sys.argv[1]
        print("Wishlist url: ", url)
        parsed_url = urlparse(url)
        if parsed_url.scheme and parsed_url.netloc:
            webpage = requests.get(url)
            soup = BeautifulSoup(webpage.text, 'html.parser')
            prices = soup.select("span.a-size-base.a-color-price")
            total_price = 0
            for each_price in prices:
                price = re.sub("[^\d\.]", "", each_price.text)
                price = price[1:] if price[0] == '.' else  price
                total_price += float(price)
            print("Total Price of your wishlist: ", total_price)
        else:
            print_error_msg("Invalid wishlist url. Exiting")
    else:
        print_error_msg("Please provide *one* wishlist url, like so: python amazon_wishlist.py http://www.url.com/path/")

if __name__ == "__main__":
    find_total_price()
