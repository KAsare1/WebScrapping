from typing import Any
import scrapy
from scrapy.http import Response

class Quotes(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response: Response, **kwargs: Any) -> Any:
        title = response.css('title::text').extract()
        yield{'titletext': title}
        # return super().parse(response, **kwargs)