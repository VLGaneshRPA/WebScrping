# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
# Credit & Course URL: https://www.udemy.com/course/web-scraping-course-in-python-bs4-selenium-and-scrapy/

import scrapy


class WorldometerSpider(scrapy.Spider):
    name = "worldometer"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        # Extracting title and country names
        title = response.xpath('//h1/text()').get()
        countries = response.xpath('//td/a/text()').getall()

    # return data extracted
        yield {
            'titles': title,
            'countries': countries,
        }
      
      
