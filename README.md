# Retail Sales Analysis & Business Insights

## Project Overview

This project analyzes retail sales data to identify profitable product categories, compare regional performance, and investigate the relationship between discounts and profit.

The goal is to turn raw sales data into actionable business insights using Python, SQL, and data visualization.

## Dataset

- **Dataset:** Sample Superstore
- **Original records:** 9,994
- **Exact duplicate rows removed:** 17
- **Cleaned records:** 9,977
- **Columns:** 13

## Tools and Technologies

- **Python** — data analysis
- **Pandas** — data cleaning and transformation
- **SQLite** — SQL-based analysis
- **Matplotlib** — data visualization
- **Seaborn** — data visualization library

## Key Business Insights

1. **Technology was the most profitable category**, generating $145,454.95 in total profit.
2. **Tables recorded the largest sub-category loss**, at $17,725.48.
3. **The West region generated the highest total profit**, at $108,329.81.
4. **Higher discount levels were associated with lower average profit** in the analyzed dataset. This association does not prove that discounts alone caused losses.

## Analysis Performed

- Dataset inspection and duplicate removal
- Sales and profit analysis by category
- Sales and profit analysis by region
- Profitability analysis by product sub-category
- Average profit analysis by discount level
- Export of SQL analysis results to CSV
- Creation of charts for business insights

## Project Structure

```text
retail-sales-analysis/
├── data/
│   ├── SampleSuperstore.csv
│   └── SampleSuperstore_Cleaned.csv
├── outputs/
│   ├── charts/
│   ├── profit_by_discount.csv
│   ├── profit_by_category.csv
│   ├── profit_by_region.csv
│   └── profit_by_subcategory.csv
├── reports/
│   └── business_insights.md
├── sql/
│   └── analysis_queries.sql
├── analyze_data.py
├── check_data.py
├── create_database.py
├── retail_sales.db
├── requirements.txt
└── README.md
```

## How to Run

1. Install Python.
2. Open a terminal in the project folder.
3. Install the required libraries:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the analysis script:

   ```bash
   python analyze_data.py
   ```

5. Create or refresh the SQLite database:

   ```bash
   python create_database.py
   ```

## Current Project Status

- [x] Data inspection and cleaning
- [x] Python analysis and charts
- [x] SQLite database creation
- [x] SQL analysis queries
- [x] Business insights report
- [x] CSV exports of SQL results
- [ ] Interactive Power BI dashboard
- [ ] GitHub documentation and publication

## Limitations

The supplied dataset does not contain order dates, order IDs, or customer IDs. Therefore, this analysis does not currently support time-series sales trends or unique-customer analysis.

## Future Improvements

- Build an interactive Power BI dashboard
- Expand the analysis with additional business questions
- Publish the project on GitHub with screenshots and documentation