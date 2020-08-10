from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import requests


baseurl = "https://www.jadroo.com/"

headers = {'user agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}


r= requests.get('https://www.jadroo.com/shop?s=t-shirt')
soup = BeautifulSoup(r.content,'lxml')
productlist = soup.find_all('div', class_='product-info text-left')

#print(productlist)

productlinks = []

for item in productlist:
    for link in item.find_all('a',href=True):       
        #print(link['href'])
        productlinks.append(link['href'])
        #print(productlinks)
    #return productlinks



#testlink= 'https://www.jadroo.com/t-shirt-and-pant-for-boys-full-set-20'

driver = webdriver.Firefox()
for link in productlinks:
    driver.get(link)
    sleep(10) # Sleep 10 seconds while waiting for the page to load...

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml") 


    '''r = requests.get(testlink, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')'''
    name = soup.find('h1', class_='name').text.strip()
    reviews = soup.find('div', class_='col-md-6 single-rating-number').text.strip()
    img = soup.find('img', {'class': 'img-responsive single-large-image featured_image'})['src']
    price=soup.find('span', {'class': 'price'}).text.strip()

    information = {
        'name':name,
        'reviews':reviews,
        'image':img,
        'price':price
    }

    print(information)
driver.close()

'''price_heading = soup.find_all('div', class_='price-box')
price = soup.find('span', class_='price')
for span in price:
    print(span.text.replace(' ৳ ','').strip())'''



'''soupprice = BeautifulSoup("""<span class="price">৳ 816.00</span>""", "lxml")
print(soupprice.string)'''



'''html_text = """
<span class="price">৳ 816.00</span>
"""

html = BeautifulSoup(html_text, "lxml")

spans = html.find_all('span', {'class': 'price'})
for span in spans:
    print(span.text.replace('৳', '').strip())


#for item in price_heading:
    #print(item)'''