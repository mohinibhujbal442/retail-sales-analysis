# Retail Sales Analysis — Business Insights

## 1. Project Overview

This project analyzes retail sales data to understand product profitability, regional performance, and the relationship between discounts and profit.

**Dataset:** Sample Superstore  
**Original records:** 9,994  
**Exact duplicate rows removed:** 17  
**Cleaned records:** 9,977

## 2. Key Business Findings

### Finding 1: Technology Is the Most Profitable Category

Technology generated the highest total profit of **$145,454.95**, followed by Office Supplies at $122,364.66. Furniture generated $18,421.81 in profit and had the lowest profit margin at 2.49%.

**Business recommendation:** Investigate Furniture pricing, product costs, and discount practices to identify opportunities to improve profitability.

### Finding 2: Tables Are a Loss-Making Sub-Category

Tables recorded a total loss of **$17,725.48**, while Bookcases recorded a loss of $3,472.56. Copiers generated the highest profit among the sub-categories, at $55,617.82.

**Business recommendation:** Review Tables pricing, costs, and discount levels before making changes to the product strategy.

### Finding 3: The West Region Performs Best

The West region generated $108,329.81 in profit with a profit margin of 14.94%. The Central region had the lowest regional profit margin at 7.92%.

**Business recommendation:** Investigate the Central region's product mix, pricing, and discount patterns to identify ways to improve profitability.

### Finding 4: Higher Discounts Are Associated With Lower Average Profit

In this dataset, orders with discounts of 30% or more generally show negative average profit across the listed discount levels, while the 0% discount group has an average profit of $67.02.

**Business recommendation:** Review high-discount transactions and evaluate whether discount policies are supporting profitable sales.

*Note: These findings show associations in the available data; they do not prove that discounts alone cause losses.*

## 3. Project Status

- [x] Load and inspect the dataset
- [x] Identify and remove exact duplicate rows
- [x] Analyze category and sub-category profitability
- [x] Analyze discount patterns
- [x] Analyze regional performance
- [x] Save three analysis charts
- [ ] Perform SQL analysis
- [ ] Build an interactive Power BI dashboard
- [ ] Complete the project README

## 4. SQL Analysis — Regional Performance

The SQL analysis shows that the West region generated the highest total profit at $108,329.81. The East region ranked second at $91,506.31.

The Central region generated $500,782.85 in sales but only $39,655.88 in profit, which was lower than the South region's $46,749.43 despite South having lower sales.

**Recommendation:** Investigate the Central region's product mix, pricing, and discount patterns to identify opportunities to improve profitability.

**SQL skills demonstrated:** `SUM()`, `ROUND()`, `GROUP BY`, and `ORDER BY`.

## 5. SQL Analysis — Product Sub-Category Performance

The SQL analysis identified Copiers as the most profitable sub-category, generating $55,617.82 in total profit. Phones ranked second with $44,515.73.

Tables recorded the largest loss at $17,725.48, while Bookcases recorded a loss of $3,472.56. Supplies also recorded a loss of $1,189.10.

**Recommendation:** Investigate the pricing, costs, and discount patterns of loss-making sub-categories, especially Tables and Bookcases, to identify opportunities to improve profitability.

**SQL skills demonstrated:** `SUM()`, `ROUND()`, `GROUP BY`, and `ORDER BY` with a column name containing a hyphen.

## 6. SQL Analysis — Discount and Profit

The SQL analysis shows that records with no discount had an average profit of $67.02. At a 20% discount, average profit was $24.72.

Discount levels of 30% and above had negative average profit in this dataset. The 50% discount group had the lowest average profit at -$310.70 per record.

**Recommendation:** Review high-discount transactions, particularly those with negative profit, to understand the role of pricing, product mix, and costs.

**SQL skills demonstrated:** `AVG()`, `SUM()`, `COUNT()`, `GROUP BY`, and `ORDER BY`.