from bs4 import BeautifulSoup
import requests

#href=[]
#def JadrooCrawler(max_pages):
    #list_of_product_details = []
    #page = 1
    #while page <= max_pages:
        #url = 'https://www.bdshop.com/search/?cat=0&q=oximeter'
        #source_code = requests.get(url)
        #plain_text = source_code.text
        #soup = BeautifulSoup(plain_text, features="html.parser")
        
        #for link in soup.findAll('a', {'class': 'product photo product-item-photo'}):
            
            #href = link.get('href')
            #print(href)
        #return href
        #return list_of_product_details
        #page+=1


#def get_product_description(product_url):
    #product_details = {}
    #meta = []
    #source_code = requests.get(product_url)
    #plain_text = source_code.text
    #soup = BeautifulSoup(plain_text,features="html.parser")

    #img     = soup.find('img', {'class': 'img-responsive single-large-image featured_image'})['src']
    #title   = soup.find('div', {'class': 'product-name'}).text
    #price   = soup.find('span', {'class': 'price-value-101419'}).text
    #p_id    = soup.find('span', {'class': 'value'}).text
    

    #print("title",title)
    #print("price",price)
    #print("p_id",p_id)



baseurl = "https://www.thewhiskyexchange.com/"

headers = {'user agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

productlinks = []

r= requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky')
soup = BeautifulSoup(r.content,features="html.parser")
productlist = soup.find_all('div', class_='item')

for item in productlist:
    for link in item.find_all('a',href=True):
        productlinks.append(baseurl + link['href'])

#print(productlinks)

#testlink= 'https://www.thewhiskyexchange.com/p/54020/nikka-from-the-barrel-jigger-2-glasses-pack'


for link in productlinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    name = soup.find('h1', class_='product-main__name').text.strip()

    price = soup.find('p', class_='product-action__price').text.strip()

    try:
        ratings = soup.find('div', class_='review-overview').text.strip()
    except:
        ratings = "not found"



    whisky = {
        'name':name,
        'ratings':ratings,
        'price':price
        }
    print(whisky)