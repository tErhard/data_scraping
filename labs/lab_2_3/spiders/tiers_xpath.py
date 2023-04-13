import scrapy
from hotline.items import HotlineItem


class TiersXpathSpider(scrapy.Spider):
    name = "tiers_xpath"
    allowed_domains = ["hotline.ua"]
    start_urls = [
        f"https://hotline.ua/ua/auto/avtoshiny-i-motoshiny/5012/?p={page}" for page in range(1, 5)]

    def parse(self, response):
        items = response.xpath('//div[contains(@class, "list-body__content")]'
            ).xpath('.//*[contains(@class,"list-item")]')
        for item in items:
            name = item.xpath('.//a[contains(@class,"list-item__title")]/text()').get()
            url = item.xpath('.//a[contains(@class,"list-item__title")]/@href').get()
            price = item.xpath('.//*[@class="price__value"]/text()').get()
            image_url = item.xpath('.//img/@src').get()
            yield HotlineItem(
                name=name,
                price=price,
                url=url,
                image_urls=[f"https://hotline.ua{image_url}"]
            )
