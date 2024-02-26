# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
# Credit & Course URL: https://www.udemy.com/course/web-scraping-course-in-python-bs4-selenium-and-scrapy/

import scrapy
import json

class QuotesapiSpider(scrapy.Spider):
    name = "quotesapi"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/api/quotes?page=1"]

    def parse(self, response):
        json_response = json.loads(response.body)
        quotes = json_response.get('quotes')
        #print(quotes)

        for quote in quotes:
            yield{
                'author':quote.get('author').get('name'),
                'tags':quote.get('tags'),
                'text':quote.get('text'),
            }