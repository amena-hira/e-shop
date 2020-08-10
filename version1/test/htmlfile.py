from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import requests



def jadroopCrawler():
    
    
    driver = webdriver.Firefox()
    link = 'https://cm10.premiummod.com/?design=cm_style2a'
    
    driver.get(link)
    sleep(1) # Sleep 10 seconds while waiting for the page to load...

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml") 
    print(soup)
       
    driver.close()
jadroopCrawler()