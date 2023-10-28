import csv
import json
import urllib.request
import argparse

from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description="Scrap products data from Shopify store")
parser.add_argument('-t', '--target', dest='website_url', type=str, help='URL to Shopify store (https://shopifystore.com)')
parser.add_argument('-v', '--variants', dest='variants',  action="store_true", help='Scrap also with variants data')
args = parser.parse_args()

if not args.website_url:
    print("usage: shopfiy_scraper.py [-h] [-t WEBSITE_URL] [-v]")
    exit(0)

base_url = args.website_url
url = base_url + '/products.json'

with_variants = args.variants


def get_page(page):
    data = urllib.request.urlopen(url + '?page={}'.format(page)).read()
    products = json.loads(data)['products']

    return products


def get_tags_from_product(product):
    r = urllib.request.urlopen(product).read()
    soup = BeautifulSoup(r, "html.parser")

    title = soup.title.string
    description = ''

    meta = soup.find_all('meta')
    for tag in meta:
        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() == 'description':
            description = tag.attrs['content'];

    return [title, description]


with open('products.csv', 'w') as f:
    page = 1

    print("[+] Starting script")

    # create file header
    writer = csv.writer(f)
    if with_variants:
        writer.writerow(['Name', 'Variant Name', 'Price', 'URL', 'Meta Title', 'Meta Description', 'Product Description'])
    else:
        writer.writerow(['Name', 'URL', 'Meta Title', 'Meta Description', 'Product Description'])

    print("[+] Checking products page")

    products = get_page(page)
    while products:
        for product in products:
            name = product['title']
            product_url = base_url + '/products/' + product['handle']
            category = product['product_type']

            body_description = BeautifulSoup(product['body_html'], "html.parser")
            body_description = body_description.get_text()


            print(" ├ Scraping: " + product_url)

            title, description = get_tags_from_product(product_url)

            if with_variants:
                for variant in product['variants']:
                    variant_name = variant['title']
                    price = variant['price']

                    row = [name, variant_name, price, product_url, title, description, body_description]
                    writer.writerow(row)
            else:
                row = [name, product_url, title, description, body_description]
                writer.writerow(row)
        page += 1
        products = get_page(page)
