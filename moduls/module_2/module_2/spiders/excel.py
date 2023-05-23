import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних з CSV-файлу
data = pd.read_csv("tv_offers.csv")

# Впорядкування пропозицій за спаданням цін
sorted_data = data.sort_values("Ціна", ascending=False)

# Збереження відсортованих даних до Excel-файлу
sorted_data.to_excel("sorted_tv_offers.xlsx", index=False)

# Побудова гістограми кількості пропозицій для кожної моделі
model_counts = data["Модель"].value_counts()
model_counts.plot.bar(figsize=(10, 6))
plt.xlabel("Модель")
plt.ylabel("Кількість пропозицій")
plt.title("Гістограма кількості пропозицій для кожної моделі")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
