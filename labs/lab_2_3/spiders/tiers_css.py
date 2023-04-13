import scrapy
from hotline.items import HotlineItem


class TiersCssSpider(scrapy.Spider):
    name = "tiers_css"
    allowed_domains = ["hotline.ua"]
    start_urls = [
        f"https://hotline.ua/ua/auto/avtoshiny-i-motoshiny/5012/?p={page}" for page in range(1, 5)]

    def parse(self, response):
        items = response.css('div.list-body__content').css('.list-item')
        for item in items:
            name = item.css('a.list-item__title::text').get()
            url = item.css('a.list-item__title::attr(href)').get()
            price = item.css('.price__value::text').get()
            image_url = item.css('img::attr(src)').get()
            yield HotlineItem(
                name=name,
                price=price,
                url=url,
                image_urls=[f"https://hotline.ua{image_url}"]
            )
