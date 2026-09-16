# DAX Measure Library

Assumes the fact table is named `FactSales` and the calendar table is `DimDate`.

```DAX
Total Revenue = SUM(FactSales[revenue])

Total Profit = SUM(FactSales[profit])

Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)

Total Orders = DISTINCTCOUNT(FactSales[order_id])

Units Sold = SUM(FactSales[quantity])

Active Customers = DISTINCTCOUNT(FactSales[customer_id])

Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)

Average Selling Price = DIVIDE([Total Revenue], [Units Sold], 0)

Revenue YTD =
TOTALYTD([Total Revenue], DimDate[date_key])

Revenue Previous Year =
CALCULATE([Total Revenue], SAMEPERIODLASTYEAR(DimDate[date_key]))

Revenue YoY Growth % =
DIVIDE([Total Revenue] - [Revenue Previous Year], [Revenue Previous Year], 0)

Revenue Previous Month =
CALCULATE([Total Revenue], DATEADD(DimDate[date_key], -1, MONTH))

Revenue MoM Growth % =
DIVIDE([Total Revenue] - [Revenue Previous Month], [Revenue Previous Month], 0)

Running Revenue =
CALCULATE(
    [Total Revenue],
    FILTER(
        ALLSELECTED(DimDate[date_key]),
        DimDate[date_key] <= MAX(DimDate[date_key])
    )
)
```

## Why measures instead of calculated columns?
Measures are evaluated in filter context at query time and are generally the correct choice for dynamic aggregations such as revenue, margin and growth. Calculated columns are materialized row-by-row and are better suited to row-level attributes that need to participate in slicing, grouping or relationships.
