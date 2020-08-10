def JadrooCrawler(max_pages,search_item):
    list_of_product_details = []
    page = 1
    while page <= max_pages:
        url = 'https://www.jadroo.com/shop?s=' + search_item + "'"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="html.parser")
        for link in soup.findAll('a', {'class': 'product photo product-item-photo'}):  
            href = link.get('href')            
            list_of_product_details.append(Jadroo_product_description(href))
            

        return list_of_product_details



def Jadroo_product_description(product_url):

        product_details = {}
        url = product_url
        source_code = requests.get(product_url)
        
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,features="html.parser")
        product_info = soup.findAll('div', {'class': 'detail-block equal-height'})
        for product in product_info:
            img     = product.find('img', {'class': 'img-responsive single-large-image featured_image'})['src']
            title   = product.find('h1', {'class': 'name'}).text
            price   = product.find('span', {'class': 'price'}).get_text()
            p_id    = product.find('span', {'class': 'value'}).text
        
            product_details = {
                'title' : title,
                'price' : price,
                'p_id' : p_id,
                'img' : img
            }
           

            return (product_details)
