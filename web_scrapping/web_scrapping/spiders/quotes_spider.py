from typing import Any
import scrapy
from scrapy.http import Response

class Quotes(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response: Response, **kwargs: Any) -> Any:
        title = response.css('title::text').extract()
        all_quotes = response.css('div.quote').extract()
        quotes = all_quotes.css('span.text::text').extract()
        author = all_quotes.css('.author::text').extract()
        yield{'title': title,
              'author': author,
              'quote':quotes
              }
        # return super().parse(response, **kwargs)