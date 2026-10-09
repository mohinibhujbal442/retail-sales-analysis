import pandas as pd
import sqlite3
from pathlib import Path

# Find the project folder
project_dir = Path(__file__).parent

# Load the cleaned CSV file
csv_path = project_dir / "data" / "SampleSuperstore_Cleaned.csv"
df = pd.read_csv(csv_path)

# Create the SQLite database
database_path = project_dir / "retail_sales.db"

with sqlite3.connect(database_path) as connection:
    df.to_sql("superstore", connection, if_exists="replace", index=False)

print("Database created successfully!")
print(f"Rows loaded: {len(df)}")
print(f"Database location: {database_path}")

# Run the first SQL query
with sqlite3.connect(database_path) as connection:
    query = """
    SELECT
        ROUND(SUM(Sales), 2) AS total_sales,
        ROUND(SUM(Profit), 2) AS total_profit,
        SUM(Quantity) AS total_quantity
    FROM superstore;
    """

    result = pd.read_sql_query(query, connection)

print("\nOverall Sales Summary:")
print(result.to_string(index=False))





# Run SQL Query 2: Profit by category
with sqlite3.connect(database_path) as connection:
    query = """
    SELECT
        Category,
        ROUND(SUM(Sales), 2) AS total_sales,
        ROUND(SUM(Profit), 2) AS total_profit
    FROM superstore
    GROUP BY Category
    ORDER BY total_profit DESC;
    """

    result = pd.read_sql_query(query, connection)

print("\nSales and Profit by Category:")
print(result.to_string(index=False))

# Run SQL Query 3: Profit by region
with sqlite3.connect(database_path) as connection:
    query = """
    SELECT
        Region,
        ROUND(SUM(Sales), 2) AS total_sales,
        ROUND(SUM(Profit), 2) AS total_profit
    FROM superstore
    GROUP BY Region
    ORDER BY total_profit DESC;
    """

    result = pd.read_sql_query(query, connection)

print("\nSales and Profit by Region:")
print(result.to_string(index=False))

# Run SQL Query 4: Profit by sub-category
with sqlite3.connect(database_path) as connection:
    query = """
    SELECT
        "Sub-Category",
        ROUND(SUM(Sales), 2) AS total_sales,
        ROUND(SUM(Profit), 2) AS total_profit
    FROM superstore
    GROUP BY "Sub-Category"
    ORDER BY total_profit DESC;
    """

    result = pd.read_sql_query(query, connection)

print("\nSales and Profit by Sub-Category:")
print(result.to_string(index=False))

# Run SQL Query 5: Profit by discount level
with sqlite3.connect(database_path) as connection:
    query = """
    SELECT
        Discount,
        ROUND(AVG(Profit), 2) AS average_profit,
        ROUND(SUM(Sales), 2) AS total_sales,
        ROUND(SUM(Profit), 2) AS total_profit,
        COUNT(*) AS number_of_records
    FROM superstore
    GROUP BY Discount
    ORDER BY Discount;
    """

    result = pd.read_sql_query(query, connection)

print("\nProfit Analysis by Discount Level:")
print(result.to_string(index=False))

# Export discount analysis results to CSV
output_dir = project_dir / "outputs"
output_dir.mkdir(parents=True, exist_ok=True)

discount_query = """
SELECT
    Discount,
    ROUND(AVG(Profit), 2) AS average_profit,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    COUNT(*) AS number_of_records
FROM superstore
GROUP BY Discount
ORDER BY Discount;
"""

with sqlite3.connect(database_path) as connection:
    discount_results = pd.read_sql_query(discount_query, connection)

discount_results.to_csv(
    output_dir / "profit_by_discount.csv",
    index=False
)

print("\nDiscount analysis exported to outputs/profit_by_discount.csv")

# Export category analysis results to CSV
category_query = """
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore
GROUP BY Category
ORDER BY total_profit DESC;
"""

with sqlite3.connect(database_path) as connection:
    category_results = pd.read_sql_query(category_query, connection)

category_results.to_csv(
    output_dir / "profit_by_category.csv",
    index=False
)

print("Category analysis exported to outputs/profit_by_category.csv")

# Export regional analysis results to CSV
region_query = """
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore
GROUP BY Region
ORDER BY total_profit DESC;
"""

with sqlite3.connect(database_path) as connection:
    region_results = pd.read_sql_query(region_query, connection)

region_results.to_csv(
    output_dir / "profit_by_region.csv",
    index=False
)

print("Regional analysis exported to outputs/profit_by_region.csv")

# Export sub-category analysis results to CSV
subcategory_query = """
SELECT
    "Sub-Category",
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore
GROUP BY "Sub-Category"
ORDER BY total_profit DESC;
"""

with sqlite3.connect(database_path) as connection:
    subcategory_results = pd.read_sql_query(
        subcategory_query, connection
    )

subcategory_results.to_csv(
    output_dir / "profit_by_subcategory.csv",
    index=False
)

print("Sub-category analysis exported to outputs/profit_by_subcategory.csv")