import requests
from bs4 import BeautifulSoup
import csv

url = "https://ek.ua/ua/list/160/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Створюємо CSV-файл та вказуємо заголовки стовпців
csv_file = open("tv_offers.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Модель", "URL зображення", "Магазин", "Ціна"])

# Отримуємо всі блоки з пропозиціями телевізорів
tv_blocks = soup.find_all("div", class_="model-short-div")

# Проходимося по кожному блоку та отримуємо потрібну інформацію
for block in tv_blocks:
    model_elem = block.find("a", class_="model-short-title")
    model = model_elem.text.strip() if model_elem else ""

    image_elem = block.find("img", class_="model-short-photo")
    image_url = image_elem["src"] if image_elem else ""

    shop_elem = block.find("div", class_="model-shop-name")
    shop = shop_elem.text.strip() if shop_elem else ""

    price_elem = block.find("div", class_="model-price-range")
    price = price_elem.text.strip() if price_elem else ""

    # Записуємо дані в CSV-файл
    csv_writer.writerow([model, image_url, shop, price])

# Закриваємо CSV-файл
csv_file.close()

print("Дані успішно збережено у файл tv_offers.csv.")
