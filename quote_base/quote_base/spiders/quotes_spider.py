import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import QuoteBaseItem


class QuotesScrapy(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]

    def start_scraping(self, response):
        open_in_browser(response)
        quotes_div = response.css('div.quote')

        items = QuoteBaseItem()

        for quotes in quotes_div:
            title_quote = quotes.css('span.text::text').extract()
            author_quote = quotes.css('.author::text').extract()
            tags_quote = quotes.css('.tag::text').extract()

            items['title'] = title_quote
            items['author'] = author_quote
            items['tags'] = tags_quote

            yield items

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'asdadas',
            'password': 'asdadada'
        }, callback=self.start_scraping)
