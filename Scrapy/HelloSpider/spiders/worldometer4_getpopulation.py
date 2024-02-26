# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
# Credit & Course URL: https://www.udemy.com/course/web-scraping-course-in-python-bs4-selenium-and-scrapy/


import scrapy

#Command: scrapy crawl worldometer4 -o population.json

class WorldometersSpider(scrapy.Spider):
    name = 'worldometer4'
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
            # yield scrapy.Request(url=absolute_url)  # sending a request with the absolute url

            # Return relative URL (sending a request with the relative url)
            yield response.follow(url=link, callback=self.parse_country, meta={'country':country_name})

    # Getting data inside the "link" website
    def parse_country(self, response):
        # Getting country names and each row element inside the population table
        country = response.request.meta['country']
        rows = response.xpath("(//table[contains(@class,'table')])[1]/tbody/tr")  # You can also use the whole class value  --> response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
        # Looping through the rows list
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()

            # Return data extracted
            yield {
                'country':country,
                'year': year,
                'population':population,
            }


