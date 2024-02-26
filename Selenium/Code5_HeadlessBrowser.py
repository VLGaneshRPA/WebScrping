# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
# Credit & Course URL: https://www.udemy.com/course/web-scraping-course-in-python-bs4-selenium-and-scrapy/


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
import pandas as pd

# Headless mode
options = Options()  # Initialize an instance of the Options class
options.headless = True  # True -> Headless mode activated
options.add_argument('window-size=1920x1080')  # Set a big window size, so all the data will be displayed

web = "https://www.audible.com/search"

path = '/Users/apple/Desktop/Python/WebScraping/chromedriver-mac-arm64/chromedriver'
driver = webdriver.Chrome(path, options=options)  # add the "options" argument to make sure the changes are applied
driver.get(web)
# driver.maximize_window()

# Locating the box that contains all the audiobooks listed in the page
container = driver.find_element(By.CLASS_NAME,value='adbl-impression-container ')

# Getting all the audiobooks listed (the "/" gives immediate child nodes)
products = container.find_elements(by='xpath',value='.//li[contains(@class, "productListItem")]')
# products = container.find_elements_by_xpath('./li')

# Initializing storage
book_title = []
book_author = []
book_length = []
# Looping through the products list (each "product" is an audiobook)
for product in products:
    # We use "contains" to search for web elements that contain a particular text, so we avoid building long XPATH
    book_title.append(product.find_element(by='xpath',value='.//h3[contains(@class, "bc-heading")]').text)  # Storing data in list
    print(book_title)
    book_author.append(product.find_element(by='xpath',value='.//li[contains(@class, "authorLabel")]').text)
    book_length.append(product.find_element(by='xpath',value='.//li[contains(@class, "runtimeLabel")]').text)

driver.quit()
# Storing the data into a DataFrame and exporting to a csv file
df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('headless_modebooks.csv', index=False)
