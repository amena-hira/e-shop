from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
from .models import ProductInfo
import requests

# Create your views here.

def BDShopCrawler(max_pages, item):

    list_of_product_details = []
    product_descrip=[]
    page = 1
    
    url = 'https://www.bdshop.com/search/?cat=0&q=' + item + "'"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    for link in soup.findAll('a', {'class': 'product photo product-item-photo'}):
        #href = link.get('href')
        list_of_product_details.append(link['href'])  

    #--------get product info-------

    productsInfo = ProductInfo.objects.filter(search_item = item)
    if productsInfo.exists():
        have="item found"
        print(have)
    else:
        product_details = {}
        
        for productts in list_of_product_details:
            source_code = requests.get(productts)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text,features="html.parser")
            product_info = soup.findAll('div', {'class': 'column main'})
            for product in product_info:
                title   = product.find('span', {'class': 'base'}).text
                price   = product.find('span', {'class': 'price'}).text
                p_id    = product.find('div', {'class' : 'value'}).text
                img     = product.find('img', {'class': 'fotorama__img'})['src']

                product_detaills = ProductInfo(title=title,price=price,img=img,search_item=item)
                product_detaills.save()
        
                '''product_details = {
                    'title' : title,
                    'price' : price,
                    'p_id'  : p_id,
                    'img'   : img,
                    'site'  : 'BDShop'
                    #'link'  : product_url,
                    #'search_item' : item
                }
            product_descrip.append(product_details)

        return (product_descrip)'''
        

def jadrooCrawler(max_pages,search_item):
    baseurl = "https://www.jadroo.com/"

    headers = {'user agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

    page= 1

    while page <= max_pages:
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
        product_description=[]
        driver = webdriver.Firefox()
        for link in productlinks:
            driver.get(link)
            sleep(10) # Sleep 10 seconds while waiting for the page to load...

            html = driver.page_source
            soup = BeautifulSoup(html, "lxml") 
            title = soup.find('h1', class_='name').text.strip()
            reviews = soup.find('div', class_='col-md-6 single-rating-number').text.strip()
            img = soup.find('img', {'class': 'img-responsive single-large-image featured_image'})['src']
            price=soup.find('span', {'class': 'price'}).text.strip()
            old_price=soup.find('span', {'class': 'price-strike'}).text.strip()


            information = {
                'title':title,
                'reviews':reviews,
                'img':img,
                'price':price,
                'old_price':old_price,
                'search_item':search_item
            }
            
            product_description.append(information)


        driver.close()

        return product_description

def PickabooCrawler(max_pages,search_item):
        list_of_product_details = []
        url = 'https://www.pickaboo.com/catalogsearch/result/?q=+' + search_item + "'"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="html.parser")
        for link in soup.findAll('a', {'class': 'product photo product-item-photo'}):
            href = link.get('href')
            list_of_product_details.append(getPickabooProductDetails(href))
        return list_of_product_details   


def getPickabooProductDetails(product_url):
    
        product_details = {}
        driver = webdriver.Firefox()

        driver.get(product_url)
        sleep(20) # Sleep 10 seconds while waiting for the page to load...

        source_code = driver.page_source
        soup = BeautifulSoup(source_code, "lxml")
        product_info = soup.findAll('div', {'class': 'column main'})
        
        for product in product_info:
            img     = product.find('img', {'class': 'fotorama__img magnify-opaque'})['src']
            brand   = product.find('div', {'class': 'manufacturer'}).find('span').text
            title   = product.find('span', {'class': 'base'}).text
            price   = product.find('span', {'class': 'price'}).text

        product_details = {
            'title' : title,
            'brand' : brand,
            'price' : price,
            'img' : img
        }

        driver.close()

        return (product_details)



def showProduct(request):
    search_item = request.GET['search_item']
    search_item.replace('','+')
    productsInfo = ProductInfo.objects.filter(search_item = search_item)
    if productsInfo.exists():
        context={
            'products':productsInfo         
        }
        return render(request, 'search_product.html', context)
    else:
        product  = BDShopCrawler(1,search_item)
    #products     += PickabooCrawler(1,search_item)
    #products     += jadrooCrawler(1,search_item)
        productsInfo = ProductInfo.objects.filter(search_item = search_item)
        context={
            'products':productsInfo
        }
        return render(request, 'search_product.html', context)
    
def single_Product(request,id):
    ProductsInfo = ProductInfo.objects.get(pk=id)
    context={
        'products':ProductsInfo,
        
    }
    return render(request, 'single_product.html', context)


def singlee_Product(request,product_title, search_item ):
    product_description = BDShopCrawler(1, search_item)

    lst = product_description
    for i, dic in enumerate(lst):
        if dic['title'] == product_title:
           index = i
    #return HttpResponse(lst)
    single_product = lst[index]
    title = single_product['title']
    price = single_product['price']
    #old_price = single_product['old_price']
    img = single_product['img']

    
    
    products=[]
    information = {
        'title' : title,
        'price' : price,
        #'old_price':old_price,
        'img'   : img
    }
    products.append(information)

    return render(request, 'single_product.html', {'products': products})

def compare(request,id1,id2):
    poducts_detail = ProductInfo.objects.get(pk=id1)
    i=ProductInfo.objects.filter(search_item = "vivo")
    productts_detail = ProductInfo.objects.get(pk=id2)
    
    if i.exists():
        item=i
        context={
            'products':i
            
        }
        return render(request, 'products.html', context)
    else:
        item="not found"
        return HttpResponse(item)
    '''context={
        'poducts_detail':poducts_detail,
        'productts_detail':productts_detail
    }
    return render(request, 'compare.html', context)'''


    
