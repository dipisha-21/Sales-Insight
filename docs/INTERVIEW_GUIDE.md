# Interview Guide

## 60-second explanation
I treated the dashboard as an analytics pipeline rather than only a visualization. Transaction data is validated first, then modelled with a sales fact table and date, customer, product and region dimensions. SQL handles quality checks and reusable analysis, while Power BI provides the semantic model and interactive reporting. I defined DAX measures for revenue, profit, margin, AOV, customer count and time intelligence such as YTD, YoY and MoM growth.

## Questions an interviewer may ask

### What is the grain?
One transaction/order-line row in `FactSales`. Defining the grain first prevents incorrect aggregations.

### Why star schema?
It separates measures from descriptive dimensions, reduces duplication and gives Power BI predictable one-to-many filtering.

### Measure vs calculated column?
Measures calculate dynamically under filter context. Calculated columns are materialized per row. Revenue and profit KPIs should normally be measures.

### What does CALCULATE do?
`CALCULATE` evaluates an expression under a modified filter context, which is why it is fundamental to DAX time intelligence and conditional metrics.

### How did you check data quality?
I check duplicate keys, invalid quantities/prices/discounts, profit reconciliation and orphan dimension keys before dashboard refresh.

### How would you improve performance?
Keep the model narrow, prefer a star schema, remove unused columns, use measures rather than unnecessary calculated columns, reduce high-cardinality fields in visuals and push appropriate transformations to SQL/source systems.

## Dashboard Story
1. Start with executive KPIs and trend.
2. Identify where revenue/profit changed.
3. Drill into product/category drivers.
4. Compare regional performance.
5. Inspect customer and channel contribution.
6. End with an actionable business observation rather than merely describing charts.

## Metric integrity
Do not quote the resume's reporting-time improvement unless you can explain the baseline, after-state and measurement method. The generated 60K-row dataset is a reproducible portfolio dataset; it is not evidence of the original business impact claim.
