# def EorangeCrawler(max_pages,search_item):
#             list_of_product_details = []
#         #page = 1
#         #while page <= max_pages:
#             url = 'https://www.eorange.shop/search?product=' + search_item + "'"
#             source_code = requests.get(url)
#             plain_text = source_code.text
#             soup = BeautifulSoup(plain_text, features="html.parser")
#             for link in soup.findAll('a', {'class': 'category_product-wrap'}):
#                 href = link.get('href')
#                 list_of_product_details.append(get_eorange_description(href))
#             return list_of_product_details
#             #page+=1


# def get_eorange_description(product_url):
#     product_details = {}
#     meta = []
#     source_code = requests.get(product_url)
#     plain_text = source_code.text
#     soup = BeautifulSoup(plain_text,features="html.parser")


#     #img     = soup.find('img', {'class': 'img-responsive single-large-image featured_image'})['src']
#     title   = soup.find('div', {'class': 'title'}).text
#     price   = soup.find('h1', {'class': 'productDetails-price'}).text
#     #p_id    = soup.find('span', {'class': 'value'}).text
#     #details = soup.find('div', { 'id' : 'product.info.description.data.items.content'})
#     #li = details
        
#     product_details = {
#         'title' : title,
#         'price' : price,
#         #'p_id' : p_id,
#         #'img' : img,
#         #'details': li
        
#     }
#     return (product_details)