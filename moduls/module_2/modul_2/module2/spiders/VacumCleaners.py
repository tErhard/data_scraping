import scrapy
from modul_2.module2.items import Module2Item
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import pandas as pd
import matplotlib.pyplot as plt


class VcSpider(scrapy.Spider):
    name = "vc"
    allowed_domains = ["ek.ua"]
    start_urls = ["https://ek.ua/list/90/"]

    def __init__(self):
        self.driver = webdriver.Chrome('/path/to/chromedriver')

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10,
                wait_until=expected_conditions.element_to_be_clickable(
                    (By.CSS_SELECTOR,
                     ".model-shop-name .sn-div")
                ),
            )

    def parse(self, response):
        self.driver.get(response.url)
        self.driver.maximize_window()
        soup = BeautifulSoup(response.text, 'html.parser')
        vcs = soup.find(id="list_form1").find_all(class_="model-short-div list-item--goods-group ms-grp")
        items = []
        for vc in vcs:
            model = vc.find(class_="u").getText()
            img_url = vc.find("img")["src"]
            price = vc.find(class_="model-conf-title").findAll("span")
            price_low, price_high = price[-2::]
            price_low = int(price_low.getText().replace("\xa0", ""))
            price_high = int(price_high.getText().replace("\xa0", ""))
            configs = vc.find(class_="conf-div-short").findAll("u")
            for config in configs:
                config = config.getText()
                item = Module2Item(
                    model=model,
                    img_url=img_url,
                    price_low=price_low,
                    price_high=price_high,
                    config=config,
                )
                items.append(item)

        # Збереження даних у таблицю Excel
        df = pd.DataFrame([item.__dict__ for item in items])
        df = df.sort_values(by='price_low')
        df.to_excel('data.xlsx', index=False)

        # Побудова діаграми кількості пропозицій для кожної моделі
        counts = df['model'].value_counts()
        plt.bar(counts.index, counts.values)
        plt.xlabel('Model')
        plt.ylabel('Count')
        plt.xticks(rotation=90)
        plt.show()

    def close(self, reason):
        self.driver.quit()


class SeleniumRequest(scrapy.Request):
    def __init__(self, wait_time=None, wait_until=None, screenshot=False, script=None, execute=None, *args, **kwargs):
        self.wait_time = wait_time
        self.wait_until = wait_until
        self.screenshot = screenshot
        self.script = script
        self.execute = execute
        super().__init__(*args, **kwargs)
