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

#f.write(headers)
for container in containers:
    brand = container.div.div.a.img['title']

    title_container = container.findAll('a',{'class':'item-title'})
    product_name = title_container[0].text

    try:
        rating = container.findAll('a', {'class':'item-rating'})
        #print(rating[0]['title'].strip('Rating + '))
    except:
        rating = "No Rating"
    #product_rating = rating[0].text

    price_container = container.findAll('li', {'class':'price-ship'})
    shipping = price_container[0].text.strip()

    print('Brand:           ' + brand)
    print('Product name:    ' + product_name)
    print('Shipping:        ' + shipping)
    #print('Rating:          ' + rating)

    #f.write(brand + ',' + product_name.replace(',', '|') + ',' + shipping + '\n')
#f.close()
