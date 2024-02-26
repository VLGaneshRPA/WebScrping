# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
# Credit & Course URL: https://www.udemy.com/course/web-scraping-course-in-python-bs4-selenium-and-scrapy/


#pip install selenium==4.9.0 

from selenium import webdriver


#download latest driver
#https://googlechromelabs.github.io/chrome-for-testing/
#https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.69/mac-arm64/chromedriver-mac-arm64.zip
#allow chromedriver from setting -> privay & settings  ->  other developer app to execute(Allow anyway) if blocked

#from selenium.webdriver.chrome.service import Service
#service =  Service('/Users/apple/Desktop/Python/WebScraping/chromedriver-mac-arm64/chromedriver')

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/Users/apple/Desktop/Python/WebScraping/chromedriver-mac-arm64/chromedriver'

driver = webdriver.Chrome(path)
driver.get(website)

driver.quit()
