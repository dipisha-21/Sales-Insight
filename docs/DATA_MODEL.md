# Data Model

## Grain
One row in `FactSales` represents one order-line transaction in the generated portfolio dataset. The grain must remain stable before defining DAX measures; mixing order-level and line-level rows would produce incorrect counts and averages.

## Star Schema
```mermaid
erDiagram
    DIM_DATE ||--o{ FACT_SALES : date
    DIM_CUSTOMER ||--o{ FACT_SALES : customer
    DIM_PRODUCT ||--o{ FACT_SALES : product
    DIM_REGION ||--o{ FACT_SALES : region

    FACT_SALES {
      string order_id PK
      date order_date FK
      string customer_id FK
      string product_id FK
      int region_key FK
      int quantity
      decimal revenue
      decimal cost
      decimal profit
    }
```

## Why a star schema?
- Keeps numeric measures in a central fact table.
- Avoids repeating descriptive product/region attributes throughout the analytical model.
- Produces simple one-to-many relationships for Power BI.
- Makes filter propagation easier to reason about.
- Supports reusable DAX measures across date, product, customer and geography dimensions.

## Power BI Relationship Guidance
Use one-to-many, single-direction relationships from each dimension to `FactSales`. Mark `DimDate` as the date table before using time-intelligence measures.

## Data Quality Contract
Before refresh, validate uniqueness of order identifiers, positive quantities/prices, discount range, profit reconciliation and dimension-key integrity. See `sql/02_data_quality.sql`.
