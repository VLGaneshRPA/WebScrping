# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
# Credit & Course URL: https://www.udemy.com/course/web-scraping-course-in-python-bs4-selenium-and-scrapy/

import scrapy

      
      
class WorldometerSpider(scrapy.Spider):
    name = "worldometer2"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        # Extracting title and country names
        #title = response.xpath('//h1/text()').get()
        countries = response.xpath('//td/a')
        
        for country in countries:
            #print('country :',country)
            country_name = country.xpath('.//text()').get()
            country_link = country.xpath('.//@href').get()
            #@print('country_name :',country_name, '  country_link :',country_link)
    # return data extracted
            yield {
                'country_name': country_name,
                'country_link': country_link,
            }


