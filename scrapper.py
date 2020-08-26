from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+card"

# opening the connection 
uClient = uReq(my_url)
page_html = uClient.read()
# closing the connection 
uClient.close()

# paring the html 
page_soup = soup(page_html, "html.parser")

# grabs each products 
items = page_soup.findAll("div", {"class": "item-container"})

print(items[0].div)
