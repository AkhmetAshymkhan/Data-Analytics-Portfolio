# Retail Sales & Inventory Analytics

End-to-end data analytics project focused on sales performance, product profitability, inventory management, and ABC-XYZ product segmentation.

The project combines **Python, SQL, and Tableau** to transform raw retail data into actionable business insights.

## Business Problem

A retail business needs to understand:

- Which products generate the most profit?
- How does profitability change over time?
- Which high-performing products are at risk of running out of stock?
- Which products are the most important for the business?
- How can products be segmented based on value and demand stability?

The goal of this project is to build an analytical workflow that answers these questions and presents the results through an interactive dashboard.

## Tools & Technologies

- **Python** — data cleaning and preparation
- **Pandas** — data transformation and analysis
- **SQL** — business queries and analytical calculations
- **Tableau** — interactive dashboard and visualization
- **Git / GitHub** — version control and project documentation

## Dashboard

### Sales & Inventory Analytics Dashboard

The Tableau dashboard provides an overview of sales performance and inventory risks.

**Main KPIs:**

- Total Units Sold: **18.7K**
- Total Profit: **₸8.02M**
- Total Products: **244**
- Average Profit per Product: **₸32.9K**

### Dashboard Features

- Monthly profit analysis
- Top 5 products by profit
- ABC-XYZ product segmentation
- Low-stock / high-profit product identification
- Month filtering
- Inventory-level filtering
- Interactive ABC-XYZ filtering
- Detailed product tooltips

## Key Insights

- **May** generated the highest monthly profit at approximately **₸2.27M**.
- The top-performing product generated approximately **₸223.2K** in profit.
- The **A-X segment** contributes approximately **₸4.41M**, making it the most valuable ABC-XYZ segment.
- Several highly profitable products have very low remaining inventory, highlighting potential stockout risks.
- ABC-XYZ segmentation helps distinguish high-value stable products from lower-value or less predictable products.

## ABC-XYZ Analysis

Products are segmented using two dimensions:

**ABC classification** evaluates products based on their contribution to business value.

- **A** — highest-value products
- **B** — medium-value products
- **C** — lower-value products

**XYZ classification** evaluates demand stability.

- **X** — stable demand
- **Y** — moderate demand variability
- **Z** — higher demand variability

Combining both classifications creates a matrix that helps prioritize inventory and product management decisions.

## Project Structure

```text
Retail-Inventory-Analytics/
├── data/
│   └── processed/
├── python/
├── sql/
├── README.md
├── requirements.txt
└── .gitignore
