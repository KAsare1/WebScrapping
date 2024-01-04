from typing import Any
import scrapy
from scrapy.http import Response
from ..items import WebScrappingItem

class Quotes(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response: Response, **kwargs: Any) -> Any:
        items = WebScrappingItem()
        title = response.css('title::text').extract()
        all_quotes = response.css('div.quote')

        for q in all_quotes:

            quotes = q.css('span.text::text').extract()
            author = q.css('.author::text').extract()

            items['author'] = author
            items['quote'] = quotes
            yield items
        
        # return super().parse(response, **kwargs)