from requests import get
from bs4 import BeautifulSoup

BASE_URL = "https://hotline.ua/"
URL = f"{BASE_URL}/ua/auto/avtoshiny-i-motoshiny/5012/"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
LAST_PAGE = 10

FILE_NAME = "tires.txt"
with open(FILE_NAME, "w", encoding="utf-8") as file:
    for p in range(1, LAST_PAGE):
        page = get(URL, headers=HEADERS, params={"p": p})
        soup = BeautifulSoup(page.content,  "html.parser")
        items = soup.find(
            name="div", class_="list-body__content").find_all(class_="list-item")
        for item in items:
            title = item.find(
                name="a", class_="list-item__title").find(string=True, recursive=False).strip()
            price = item.find(class_="price__value").find(
                string=True, recursive=False)

            print(f"Title: {title}")
            print(f"Price: {price}")
            file.write(f"Title: {title}\n")
            file.write(f"Price: {price}\n")
