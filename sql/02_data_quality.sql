-- Data-quality checks to run before dashboard refresh.

-- Duplicate order identifiers: expected 0 rows
SELECT order_id, COUNT(*) duplicate_count
FROM fact_sales
GROUP BY order_id
HAVING COUNT(*) > 1;

-- Invalid commercial values: expected 0
SELECT COUNT(*) invalid_rows
FROM fact_sales
WHERE quantity <= 0 OR unit_price < 0 OR discount_pct NOT BETWEEN 0 AND 100;

-- Reconciliation: profit should equal revenue - cost
SELECT COUNT(*) reconciliation_failures
FROM fact_sales
WHERE ABS(profit - (revenue - cost)) > 0.01;

-- Missing dimension relationships: expected 0
SELECT COUNT(*) orphan_products
FROM fact_sales f
LEFT JOIN dim_product p ON p.product_id = f.product_id
WHERE p.product_id IS NULL;

-- Useful refresh diagnostics
SELECT MIN(order_date) min_order_date,
       MAX(order_date) max_order_date,
       COUNT(*) row_count,
       COUNT(DISTINCT customer_id) customer_count
FROM fact_sales;
