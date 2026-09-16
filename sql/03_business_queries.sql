-- Monthly revenue and profitability trend
SELECT EXTRACT(YEAR FROM order_date) AS sales_year,
       EXTRACT(MONTH FROM order_date) AS sales_month,
       SUM(revenue) AS revenue,
       SUM(profit) AS profit,
       ROUND(100.0 * SUM(profit) / NULLIF(SUM(revenue), 0), 2) AS margin_pct
FROM fact_sales
GROUP BY EXTRACT(YEAR FROM order_date), EXTRACT(MONTH FROM order_date)
ORDER BY sales_year, sales_month;

-- Product/category profitability
SELECT p.category, p.sub_category,
       SUM(f.revenue) revenue,
       SUM(f.profit) profit,
       SUM(f.quantity) units_sold
FROM fact_sales f
JOIN dim_product p ON p.product_id = f.product_id
GROUP BY p.category, p.sub_category
ORDER BY profit DESC;

-- Top three products within each region
WITH product_region AS (
    SELECT r.region, p.product_name, SUM(f.revenue) revenue
    FROM fact_sales f
    JOIN dim_product p ON p.product_id = f.product_id
    JOIN dim_region r ON r.region_key = f.region_key
    GROUP BY r.region, p.product_name
), ranked AS (
    SELECT product_region.*,
           DENSE_RANK() OVER (PARTITION BY region ORDER BY revenue DESC) revenue_rank
    FROM product_region
)
SELECT * FROM ranked WHERE revenue_rank <= 3
ORDER BY region, revenue_rank;

-- Highest-value customers
SELECT customer_id,
       COUNT(DISTINCT order_id) order_count,
       SUM(revenue) lifetime_revenue,
       SUM(profit) lifetime_profit,
       RANK() OVER (ORDER BY SUM(revenue) DESC) customer_rank
FROM fact_sales
GROUP BY customer_id
ORDER BY customer_rank;

-- Channel mix
SELECT sales_channel,
       COUNT(*) orders,
       SUM(revenue) revenue,
       ROUND(100.0 * SUM(revenue) / SUM(SUM(revenue)) OVER (), 2) revenue_share_pct
FROM fact_sales
GROUP BY sales_channel
ORDER BY revenue DESC;
