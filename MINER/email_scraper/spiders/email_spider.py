import scrapy
import re

class EmailSpider(scrapy.Spider):
    name = "email_spider"
    start_urls = ["https://brave.com"]  # Replace with the starting URL

    def parse(self, response):
        # Extract email addresses using regular expressions
        email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}'
        #email_pattern = r'[A-Za-z0-9._%+-]+@+"brave.com"'
        emails = re.findall(email_pattern, response.text)

        for email in emails:
            yield {
                'email': email
            }

        # Follow links to other pages recursively
        for next_page in response.css('a::attr(href)').extract():
            if next_page:
                yield response.follow(next_page, self.parse)

