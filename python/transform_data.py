import pandas as pd

# Загружаем Excel
df = pd.read_excel(
    "data/raw/Alatau Home ABCnXYZ.xlsx",
    header=1
)

# Удаляем пустую колонку
df = df.drop(columns=["Unnamed: 0"])

# Удаляем полностью пустые строки
df = df.dropna(how="all")

# Удаляем строки без названия товара
df = df.dropna(subset=["Товар"])

# Приводим числовые столбцы к числам
numeric_columns = [
    "Закупочная цена",
    "Цена продажи",
    "Продано за Апрель",
    "Продано за Май",
    "Продано за Июнь",
    "Продано за Июль",
    "Остаток",
    "Прибыль за Апрель",
    "Прибыль за Май",
    "Прибыль за Июнь",
    "Прибыль за Июль"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Проверяем результат
print(df.info())
print(df.head())