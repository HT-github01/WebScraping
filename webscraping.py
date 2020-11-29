# -*- coding: utf-8 -*-
"""WebScraping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s9wbfe48MKA5iPoddRC8aiuuY_GGLig_
"""

!pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import pandas as pd 

#opening up the connection with the URL
url = "https://store.playstation.com/en-my/category/7d7c7838-1ee7-44bc-a9fb-89148ab93899/1"
source = requests.get(url).text

#html parsing
soup = BeautifulSoup(source, 'html.parser')

#grabs each product
containers = soup.findAll("div",{"class":"ems-sdk-product-tile"})

#see the total length of the products that we selected
len(containers)

#get the html code of containers
containers[0]

# Commented out IPython magic to ensure Python compatibility.
# %%writefile test.html
# 
# < div class="ems-sdk-product-tile" data - qa="ems-sdk-product-tile" data - qa - index="0">
#     < a class="ems-sdk-product-tile-link" data - telemetry - meta='{"id":"JP0571-CUSA24959_00-HAMPRDC000000001","index":0,"name":"Arcade Archives Green Beret (English, Japanese)","price":"RM 33.00"}' data - track - click="web:store:product-tile" data - track - content="web:store:product-tile" href="/en-my/product/JP0571-CUSA24959_00-HAMPRDC000000001" title="Arcade Archives Green Beret (English, Japanese)">
#         < div class="ems-sdk-product-tile-image" data - qa="ems-sdk-product-tile-image">
#             < div class="ems-sdk-product-tile-image__container">
#                 < span class="psw-illustration psw-illustration--default-product-image default-product-img" data - qa="">
#                     < svg>
#                         < title>
#                             < /title>
#                                 <use href="#ps-illustration:default-product-image"></use>
#                                 < /svg></span>
#                                     < span class="psw-media-frame psw-fill-x psw-image psw-aspect-1-1" data - qa="ems-sdk-product-tile-image-img" style="width:100%;min-width:100%">
#                                         < img alt="Arcade Archives Green Beret (English, Japanese)" aria - hidden="true" class="psw-blur psw-top-left psw-l-fit-cover" data - qa="ems-sdk-product-tile-image-img#preview" loading="lazy" src="https://image.api.playstation.com/vulcan/ap/rnd/202011/1607/I915uitaRx4WkIyLY9J4caRr.png?w=54&amp;thumb=true" />
#                                         < noscript class="psw-layer">
#                                             < img alt="Arcade Archives Green Beret (English, Japanese)" class="psw-top-left psw-l-fit-cover" data - qa="ems-sdk-product-tile-image-img#image-no-js" loading="lazy" src="https://image.api.playstation.com/vulcan/ap/rnd/202011/1607/I915uitaRx4WkIyLY9J4caRr.png" />
#                                             < /noscript></span>
#                                                 < /div>
#                                                     <div class="ems-sdk-product-tile-image__badge-container psw-m-r-3xs"><span class="psw-p-x-3xs ems-sdk-product-tile-image__badge" data-qa="ems-sdk-product-tile-image-badge">PS4</span>
#                                                         < /div>
#                                                     </div>
#                                                     < section class="ems-sdk-product-tile__details" data - qa="ems-sdk-product-tile-details">
#                                                         < span class="body-2 truncate-text-2 psw-p-t-2xs" data - qa="ems-sdk-product-tile-name"> Arcade Archives Green Beret(English, Japanese) < /span>
#                                                                 <div class="price__container"><span class="price" data-qa="ems-sdk-product-tile-price">RM 33.00</span>
#                                                                     < /div>
#                                                                         </section>
#                                                                         < /a>
#                                                                 </div>

container = containers[0]

#scrap the name of product
container.img["alt"]

#scrap the price of product
price_container = container.findAll("span",{"class":"price"})
price_container[0].text

#create an array to store all the scrap info
#store the scrap info into dataframe
scrap = []

for container in containers:
  product_name = container.img["alt"]
  price_container = container.findAll("span",{"class":"price"})
  product_price = price_container[0].text

  print(product_name)
  print(product_price)
  print()

  scrap.append([product_name,product_price])
df = pd.DataFrame.from_records(data=scrap,columns=['product name','product price'])
df.head()

#store the data into specify csv file
df.to_csv("WebScraping.csv")