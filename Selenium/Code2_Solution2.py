# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
# Credit & Course URL: https://www.udemy.com/course/web-scraping-course-in-python-bs4-selenium-and-scrapy/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

# define the website to scrape and path where the chromediver is located
website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/Users/frankandrade/Downloads/chromedriver'  # write your path here
service = Service(executable_path=path)  # selenium 4
driver = webdriver.Chrome(service=service)  # define 'driver' variable
# open Google Chrome with chromedriver
driver.get(website)

# locate and click on a button
all_matches_button = driver.find_element(by='xpath', value='//label[@analytics-event="All matches"]')
all_matches_button.click()

# select elements in the table
matches = driver.find_elements(by='xpath', value='//tr')

# storage data in lists
date = []
home_team = []
score = []
away_team = []

# looping through the matches list
for match in matches:
    date.append(match.find_element(by='xpath', value='./td[1]').text)
    home = match.find_element(by='xpath', value='./td[2]').text
    home_team.append(home)
    print(home)
    score.append(match.find_element(by='xpath', value='./td[3]').text)
    away_team.append(match.find_element(by='xpath', value='./td[4]').text)
# quit drive we opened at the beginning
driver.quit()

# Create Dataframe in Pandas and export to CSV (Excel)
df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv('football_data.csv', index=False)
print(df)
