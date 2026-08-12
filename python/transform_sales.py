import pandas as pd

# Загружаем Excel
df = pd.read_excel(
    "data/raw/Alatau Home ABCnXYZ.xlsx",
    header=1
)

# Удаляем пустую колонку
df = df.drop(columns=["Unnamed: 0"])

# Удаляем пустые строки
df = df.dropna(subset=["Товар"])

# Преобразуем таблицу продаж в "длинный" формат
sales = pd.melt(
    df,
    id_vars=["Товар"],
    value_vars=[
        "Продано за Апрель",
        "Продано за Май",
        "Продано за Июнь",
        "Продано за Июль"
    ],
    var_name="Month",
    value_name="Units Sold"
)

# Оставляем только название месяца
sales["Month"] = sales["Month"].str.replace("Продано за ", "", regex=False)

# Приводим продажи к целому числу
sales["Units Sold"] = sales["Units Sold"].astype(int)

# Сохраняем CSV
sales.to_csv(
    "data/processed/sales.csv",
    index=False,
    encoding="utf-8-sig"
)

print("sales.csv успешно сохранен!")
print(sales.head(20))