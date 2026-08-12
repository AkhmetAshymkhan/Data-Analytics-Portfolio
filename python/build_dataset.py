import pandas as pd

# ==========================
# Load and clean source data
# ==========================

df = pd.read_excel(
    "data/raw/Alatau Home ABCnXYZ.xlsx",
    header=1
)

# Remove empty first column
df = df.drop(columns=["Unnamed: 0"])

# Remove empty rows
df = df.dropna(subset=["Товар"])

# Convert numeric columns
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

# ==========================
# Build Products table
# ==========================

products = df[[
    "Товар",
    "Закупочная цена",
    "Цена продажи",
    "Остаток"
]].copy()

products.insert(0, "Product ID", range(1, len(products) + 1))

products.to_csv(
    "data/processed/products.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Products table created!")

# ==========================
# Build Sales Fact table
# ==========================

months = ["Апрель", "Май", "Июнь", "Июль"]

sales_rows = []

for index, row in df.iterrows():

    product_id = index + 1

    for month in months:

        sales_rows.append({
            "Product ID": product_id,
            "Month": month,
            "Units Sold": int(row[f"Продано за {month}"]),
            "Profit": float(row[f"Прибыль за {month}"]),
            "ABC": row[f"ABC по прибыли {month}"],
            "XYZ": row["XYZ Классификация"]
        })

sales = pd.DataFrame(sales_rows)

sales.to_csv(
    "data/processed/sales.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Sales table created!")
print(sales.head())
print(f"\nTotal rows: {len(sales)}")