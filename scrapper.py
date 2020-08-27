from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/p/pl?Submit=StoreIM&Category=38&Depa=1"

# opening the connection 
uClient = uReq(my_url)
page_html = uClient.read()
# closing the connection 
uClient.close()

# paring the html 
page_soup = soup(page_html, "html.parser")

# grabs each products 
containers = page_soup.findAll("div", {"class": "item-container"})

# saving to csv
filename = "products.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping, price\n"
f.write(headers)

# looping through the items
for container in containers:
    # getting the brand name
    brand = container.div.div.a.img["title"]
    # getting the title
    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    # getting the shipping information
    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text

    # getting the product price
    price_container = container.findAll("li", {"class": "price-current"})
    price_big = price_container[0].strong.text
    price_small = price_container[0].sup.text
    full_price = price_big + price_small

    print(brand)
    print(product_name)
    print(shipping)
    print(full_price)
    print("\n")

    f.write(f"{brand} , {product_name.replace(',', '|')} , {shipping} , {full_price} \n")

f.close()