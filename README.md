# Sales Insight Dashboard

End-to-end sales analytics portfolio project using **SQL, Power BI and DAX**. The repository demonstrates a reproducible workflow from raw transactional data to a star-schema analytical model, business KPIs and an interactive dashboard.

## Business Problem
A sales team needs one reliable view of revenue, profitability, orders, products, customers and regional performance. The project turns transaction-level data into decision-ready metrics and dashboard views.

## Tech Stack
- Power BI
- DAX
- SQL
- Python (reproducible synthetic data generation)
- CSV / Excel-compatible data

## Data Pipeline
```text
Raw Sales Data
      ↓
Validation & Cleaning
      ↓
SQL Transformations
      ↓
Star Schema
      ↓
DAX Measures
      ↓
Power BI Dashboard
      ↓
Business Insights
```

## Analytical Model
```text
DimDate ─────┐
DimCustomer ─┤
DimProduct ──┼── FactSales
DimRegion ───┘
```

## Core KPIs
- Total Revenue
- Total Profit
- Profit Margin %
- Total Orders
- Average Order Value
- Units Sold
- Active Customers
- Revenue YTD
- Revenue YoY Growth %
- Revenue MoM Growth %
- Top Product / Category / Region analysis

## Repository Structure
```text
Sales Insight.pbix            Existing Power BI report
scripts/generate_sales_data.py
sql/01_schema.sql
sql/02_data_quality.sql
sql/03_business_queries.sql
dax/measures.md
docs/DATA_MODEL.md
docs/INTERVIEW_GUIDE.md
.github/workflows/data-checks.yml
```

## Reproducible Dataset
`scripts/generate_sales_data.py` creates **60,000 deterministic synthetic transaction rows** using a fixed seed. This provides a portfolio-safe dataset large enough to demonstrate aggregation, modelling and BI workflows without exposing business/customer data.

```bash
python scripts/generate_sales_data.py
```

The generated file is `data/generated_sales.csv`.

## Power BI
The existing `.pbix` report is retained. The DAX documentation in this upgrade provides reusable KPI definitions for the model. A strong dashboard layout is:

1. **Executive Overview** — revenue, profit, margin, orders, AOV and trends
2. **Product Performance** — category/sub-category/product contribution
3. **Regional Analysis** — region/state revenue and profitability
4. **Customer Analysis** — customer value, order frequency and channel mix

## SQL Analysis
The SQL layer includes data-quality checks and interview-relevant analysis using CTEs, aggregation and window functions: monthly trends, category profitability, top products by region and customer ranking.

## Important Note on Metrics
This repository does **not** manufacture a performance-improvement percentage. Any claim such as “reduced reporting time by 30%” should only be used when backed by an actual before/after measurement from the original project.

## Interview Talking Points
Be ready to explain the grain of `FactSales`, why a star schema was chosen, calculated columns vs measures, filter context, `CALCULATE`, time intelligence, data-quality checks and how SQL and Power BI divide responsibilities.

## Author
Dipisha Shivangi
