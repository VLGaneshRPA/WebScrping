# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
# Credit & Course URL: https://www.udemy.com/course/web-scraping-course-in-python-bs4-selenium-and-scrapy/

import scrapy
import json

class QuotesapiSpider(scrapy.Spider):
    name = "quotesapi-page"
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
            
        print('page number is ======== ',json_response.get('page'))
        
        # Picking the "has_next" element
        has_next = json_response.get('has_next')

        # If has_next==True (there's next page), execute the following code
        if has_next:
            next_page_number = json_response.get('page')+1
            yield scrapy.Request(
                url=f'https://quotes.toscrape.com/api/quotes?page={next_page_number}',
                callback=self.parse
            )