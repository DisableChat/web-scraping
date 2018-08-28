##
# Creator: MagikarpUsedFly
##

##
# The purpose of this script is to dabble in the BeautifulSoup if you will.
# Where the main outline/objective is to webscrape the sight newegg for info
# for some hardware.
##


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


# Hardcoded URL for the newegg Gpu section.
URL = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'


# Setting up a connection and then grabbing information from the page.
obj_site = uReq(URL)
sitePage_html = obj_site.read()
obj_site.close()

# Parsing
soup_page = soup(sitePage_html, 'html.parser')

# Print Html info for site
#print(soup_page.h1)

# Pulling each product
containers = soup_page.findAll('div', {'class':'item-container'})
#print(containers[0])

filename = 'products.csv'
#f = open(filename, 'w')
#headers = 'brand, product_name, shipping\n'
