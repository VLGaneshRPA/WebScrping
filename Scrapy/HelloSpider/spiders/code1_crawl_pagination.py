# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
# Credit & Course URL: https://www.udemy.com/course/web-scraping-course-in-python-bs4-selenium-and-scrapy/

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TranscriptsSpider(CrawlSpider):
    name = 'transcriptspage'
    allowed_domains = ['subslikescript.com']
    start_urls = ['https://subslikescript.com/movies_letter-X']  # let's test scraping all the pages for the X letter

    # Setting rules for the crawler
    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='scripts-list']/a")), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=("(//a[@rel='next'])[1]"))),
    )

    def parse_item(self, response):
        # Getting the article box that contains the data we want (title, plot, etc)
        article = response.xpath("//article[@class='main-article']")
        
         # Note: For SQLLite.getall() will return a list, use .join() to turn the list into a string
        transcript_list = article.xpath("./div[@class='full-script']/text()").getall()
        transcript_string = ' '.join(transcript_list)
        # Extract the data we want and then yield it
        yield {
            'title':article.xpath("./h1/text()").get(),
            'plot':article.xpath("./p/text()").get(),
            'transcript':transcript_string,
            'url':response.url,
        }
