import scrapy
from ..items import QuoteBaseItem


class QuotesScrapy(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
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
