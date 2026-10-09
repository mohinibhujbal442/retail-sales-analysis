
import pandas as pd
from pathlib import Path

file_path = Path(__file__).parent / "data" / "SampleSuperstore.csv"

df = pd.read_csv(file_path)

print("Dataset shape:", df.shape)

print("\nColumn data types:")
print(df.dtypes)

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nNumerical summary:")
print(df[["Sales", "Quantity", "Discount", "Profit"]].describe())


print("\nFirst 10 duplicate rows:")
print(df[df.duplicated(keep=False)].head(10))


clean_df = df.drop_duplicates()

print("\nOriginal row count:", len(df))
print("Row count after removing exact duplicates:", len(clean_df))
print("Duplicate rows removed:", len(df) - len(clean_df))


clean_df.to_csv(
    Path(__file__).parent / "data" / "SampleSuperstore_Cleaned.csv",
    index=False
)
print("\nCleaned dataset saved successfully!")


print("\nProfit and sales by category:")

category_summary = (
    clean_df.groupby("Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Units_Sold=("Quantity", "sum")
    )
    .round(2)
    .sort_values("Total_Profit", ascending=False)
)

print(category_summary)


category_summary["Profit_Margin_%"] = (
    category_summary["Total_Profit"]
    / category_summary["Total_Sales"]
    * 100
).round(2)

print("\nCategory profitability with profit margin:")
print(category_summary)


subcategory_summary = (
    clean_df.groupby("Sub-Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Units_Sold=("Quantity", "sum")
    )
    .round(2)
    .sort_values("Total_Profit", ascending=False)
)

print("\nTop 5 most profitable sub-categories:")
print(subcategory_summary.head(5))

print("\nBottom 5 sub-categories by profit:")
print(subcategory_summary.tail(5))


import matplotlib.pyplot as plt

profit_by_subcategory = subcategory_summary.sort_values("Total_Profit")

plt.figure(figsize=(10, 7))
profit_by_subcategory["Total_Profit"].plot(
    kind="barh",
    color=[
        "tomato" if profit < 0 else "seagreen"
        for profit in profit_by_subcategory["Total_Profit"]
    ]
)

plt.title("Profit by Product Sub-Category")
plt.xlabel("Total Profit")
plt.ylabel("Sub-Category")
plt.axvline(0, color="black", linewidth=0.8)
plt.tight_layout()

output_dir = Path(__file__).parent / "outputs" / "charts"
output_dir.mkdir(parents=True, exist_ok=True)

plt.savefig(output_dir / "profit_by_subcategory.png", dpi=150)
plt.show()

print("\nChart saved to outputs/charts/profit_by_subcategory.png")


discount_summary = (
    clean_df.groupby("Discount")
    .agg(
        Average_Profit=("Profit", "mean"),
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Number_of_Rows=("Profit", "count")
    )
    .round(2)
    .sort_index()
)

print("\nProfit analysis by discount level:")
print(discount_summary)


plt.figure(figsize=(10, 6))

discount_summary["Average_Profit"].plot(
    kind="bar",
    color=[
        "seagreen" if profit >= 0 else "tomato"
        for profit in discount_summary["Average_Profit"]
    ]
)

plt.title("Average Profit by Discount Level")
plt.xlabel("Discount")
plt.ylabel("Average Profit")
plt.axhline(0, color="black", linewidth=0.8)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    output_dir / "average_profit_by_discount.png",
    dpi=150
)
plt.show()

print("\nDiscount chart saved successfully!")


region_summary = (
    clean_df.groupby("Region")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Units_Sold=("Quantity", "sum")
    )
    .round(2)
    .sort_values("Total_Profit", ascending=False)
)

print("\nSales and profit by region:")
print(region_summary)


region_summary["Profit_Margin_%"] = (
    region_summary["Total_Profit"]
    / region_summary["Total_Sales"]
    * 100
).round(2)

print("\nRegional profitability:")
print(region_summary)


plt.figure(figsize=(8, 5))

region_summary["Total_Profit"].sort_values().plot(
    kind="bar",
    color="steelblue"
)

plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    output_dir / "profit_by_region.png",
    dpi=150
)
plt.show()

print("\nRegional profit chart saved successfully!")



