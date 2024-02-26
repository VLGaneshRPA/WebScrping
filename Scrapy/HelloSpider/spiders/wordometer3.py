# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
# Credit & Course URL: https://www.udemy.com/course/web-scraping-course-in-python-bs4-selenium-and-scrapy/

import scrapy


class WorldometersSpider(scrapy.Spider):
    name = 'worldometer3'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # Extracting "a" elements for each country
        countries = response.xpath('//td/a')

        # Looping through the countries list
        for country in countries:
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # Absolute URL
            # absolute_url = f'https://www.worldometers.info/{link}'  # concatenating links with f-string
            # absolute_url = response.urljoin(link)  # concatenating links with urljoin
            # yield scrapy.Request(url=absolute_url) # sending a request with the absolute url

            # Return relative URL
            yield response.follow(url=link)  # sending a request with the relative url