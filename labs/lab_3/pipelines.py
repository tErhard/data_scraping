import pandas as pd
from PIL import Image
import numpy as np
import sqlite3


# Розробка пайплайну для очищення даних

def clean_data(data):
    # Видалення дублікатів даних
    data.drop_duplicates(inplace=True)

    # Видалення непотрібної інформації
    data.drop(columns=['unnecessary_column'], inplace=True)

    # Видалення пустих значень
    data.dropna(inplace=True)

    # Заміна пропущених значень
    data.fillna(0, inplace=True)

    return data

data = pd.read_csv('data.csv')
data = clean_data(data)


# Налаштування пайплайну для завантаження зображень

def load_image(image_path, new_size):
    # Завантаження зображення з джерела
    img = Image.open(image_path)

    # Зміна розміру зображення
    img = img.resize(new_size)

    # Перетворення зображення в числовий формат
    img_array = np.array(img)

    return img_array

img_path = 'image.jpg'
new_size = (100, 100)
img_array = load_image(img_path, new_size)



# Збереження зібраних даних до бази даних


def save_data_to_db(data):
    # Підключення до бази даних
    conn = sqlite3.connect('database.db')

    # Створення таблиці для збереження даних
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE data
                      (column1 INTEGER, column2 INTEGER, column3 INTEGER)''')

    # Збереження даних до таблиці
    data.to_sql('data', conn, if_exists='replace', index=False)

data = pd.read_csv('data.csv')
save_data_to_db(data)


