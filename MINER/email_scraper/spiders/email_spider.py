import scrapy
import re

import ssl


print("""\
               __                               
              /  |                              
 _____  ____  $$/  _______    ______    ______  
/     \/    \ /  |/       \  /      \  /      \ 
$$$$$$ $$$$  |$$ |$$$$$$$  |/$$$$$$  |/$$$$$$  |
$$ | $$ | $$ |$$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
$$ | $$ | $$ |$$ |$$ |  $$ |$$$$$$$$/ $$ |      
$$ | $$ | $$ |$$ |$$ |  $$ |$$       |$$ |      
$$/  $$/  $$/ $$/ $$/   $$/  $$$$$$$/ $$/       
------------------------------------------                                               
------------------------------------------""")

ctx = ssl.create_default_context() #ignore ssl certification error with this 3 lines
ctx.check_hostname = False
ctx.verify_mode= ssl.CERT_NONE


class EmailSpider(scrapy.Spider):
    name = "email_spider"

    def start_requests(self):
        user_input = input("Enter the starting URL: ")
        self.start_urls = [user_input]

        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Extract email addresses using regular expressions
        email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}'
        emails = re.findall(email_pattern, response.text)

        for email in emails:
            yield {
                'email': email
            }

        # Follow links to other pages recursively
        for next_page in response.css('a::attr(href)').extract():
            if next_page:
                yield response.follow(next_page, self.parse)
