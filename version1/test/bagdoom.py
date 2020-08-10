from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep


url = 'https://www.jadroo.com/t-shirt-and-pant-for-boys-full-set-20'

driver = webdriver.Firefox()

driver.get(url)
sleep(10) # Sleep 10 seconds while waiting for the page to load...

html = driver.page_source
soup = BeautifulSoup(html, "lxml") 
spans=soup.find('span', {'class': 'price'}).text.strip()

print(spans)

driver.close()