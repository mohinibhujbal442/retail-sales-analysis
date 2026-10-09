-- Retail Sales Analysis
-- Query 1: Calculate total sales, total profit, and total quantity sold.

SELECT
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    SUM(Quantity) AS total_quantity
FROM superstore;

-- Query 2: Compare sales and profit by category

SELECT
    Category,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore
GROUP BY Category
ORDER BY total_profit DESC;

-- Query 3: Compare sales and profit by region

SELECT
    Region,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore
GROUP BY Region
ORDER BY total_profit DESC;

-- Query 4: Find the most and least profitable sub-categories

SELECT
    "Sub-Category",
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM superstore
GROUP BY "Sub-Category"
ORDER BY total_profit DESC;

-- Query 5: Analyze profit by discount level

SELECT
    Discount,
    ROUND(AVG(Profit), 2) AS average_profit,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    COUNT(*) AS number_of_records
FROM superstore
GROUP BY Discount
ORDER BY Discount;