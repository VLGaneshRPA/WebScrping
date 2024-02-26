# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
# Credit & Course URL: https://www.udemy.com/course/web-scraping-course-in-python-bs4-selenium-and-scrapy/

import scrapy


class AudibleSpider(scrapy.Spider):
    name = 'scrapaudiblepage'
    allowed_domains = ['www.audible.com']
    start_urls = ['https://www.audible.com/search/']

    def parse(self, response):
        # Getting the box that contains all the info we want (title, author, length)
        # product_container = response.xpath('//div[@class="adbl-impression-container "]/li')
        product_container = response.xpath('//div[@class="adbl-impression-container "]//li[contains(@class, "productListItem")]')

        # Looping through each product listed in the product_container box
        for product in product_container:
            book_title = product.xpath('.//h3[contains(@class, "bc-heading")]/a/text()').get()
            book_author = product.xpath('.//li[contains(@class, "authorLabel")]/span/a/text()').getall()
            book_length = product.xpath('.//li[contains(@class, "runtimeLabel")]/span/text()').get()

            # Return data extracted
            yield {
                'title': book_title,
                'author': book_author,
                'length': book_length,
            }
             # Getting the pagination bar (pagination) and then the link within the next page button (next_page_url)
        pagination = response.xpath('//ul[contains(@class , "pagingElements")]')
        next_page_url = pagination.xpath('.//span[contains(@class , "nextButton")]/a/@href').get()
        button_disabled = pagination.xpath('.//span[contains(@class , "nextButton")]/a/@aria-disabled').get()

        # Going to the "next_page_url" link
        if next_page_url and button_disabled==None:
            yield response.follow(url=next_page_url, callback=self.parse)
