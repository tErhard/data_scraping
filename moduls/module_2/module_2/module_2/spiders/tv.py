import scrapy


class TvSpider(scrapy.Spider):
    name = "tv"
    allowed_domains = ["ek.ua"]
    start_urls = ["https://ek.ua/ua/list/160/"]

    def parse(self, response):
        pass
