from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import requests



def jadroopCrawler(search_item):
    baseurl = "https://www.jadroo.com/"

    headers = {'user agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    url = 'https://www.jadroo.com/shop?s=' + search_item 
    print(url)
    r= requests.get(url)
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
    information = {}
    driver = webdriver.Firefox()
    for link in productlinks:
        driver.get(link)
        sleep(10) # Sleep 10 seconds while waiting for the page to load...

        html = driver.page_source
        soup = BeautifulSoup(html, "lxml") 
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
        return information
    driver.close()
    

print(jadroopCrawler('t-shirt'))