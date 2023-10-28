# Shopify Products Scraper

This is Shopify products Scraper. The script retrieves data from the products.json file of Shopify shop. 
Then, for each product, it makes an additional query to the 
product page to retrieve data from meta tags.

All scraped information is saved to a CSV file (products.csv)

### Installation
```
git clone https://github.com/grabowskiadrian/shopify-products-scraper.git
cd shopify-products-scraper
pip3 install -r requirements.txt
```

### Usage

```
python3 shopfiy_scraper.py -t https://www.shopifyshop.com
```

Output:

```
python3 shopfiy_scraper.py -t https://www.shopifyshop.com
[+] Starting script
[+] Checking products page
 ├ Scraping: https://www.shopifyshop.com/products/nami-nude-corn-outlet
 ├ Scraping: https://www.shopifyshop.com/products/sniegowce-damskie-czarne-boom-snow-boots-black-grape
 ├ Scraping: https://www.shopifyshop.com/products/mini-pouch-mokka-croco
 ├ Scraping: https://www.shopifyshop.com/products/saszetka-etui-na-karty-damskie-mini-pouch-black-ink-croco
 ...
[+] Scraping done
 ```