import scrapy
from ..items import QuoteBaseItem


class QuotesScrapy(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        'https://quotes.toscrape.com/page/1/'
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

        next_page = 'https://quotes.toscrape.com/page/' + str(QuotesScrapy.page_number)+ '/'

        if QuotesScrapy.page_number < 11:
            QuotesScrapy.page_number += 1
            yield response.follow(next_page, callback=self.parse)