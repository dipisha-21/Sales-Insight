-- Portable analytical star schema (adapt data types as needed for your SQL engine)
CREATE TABLE dim_date (
    date_key DATE PRIMARY KEY,
    year_number INTEGER NOT NULL,
    quarter_number INTEGER NOT NULL,
    month_number INTEGER NOT NULL,
    month_name VARCHAR(20) NOT NULL
);

CREATE TABLE dim_customer (
    customer_id VARCHAR(20) PRIMARY KEY
);

CREATE TABLE dim_product (
    product_id VARCHAR(20) PRIMARY KEY,
    product_name VARCHAR(120) NOT NULL,
    category VARCHAR(80) NOT NULL,
    sub_category VARCHAR(80) NOT NULL
);

CREATE TABLE dim_region (
    region_key INTEGER PRIMARY KEY,
    region VARCHAR(40) NOT NULL,
    state VARCHAR(80) NOT NULL,
    UNIQUE(region, state)
);

CREATE TABLE fact_sales (
    order_id VARCHAR(30) PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_id VARCHAR(20) NOT NULL,
    product_id VARCHAR(20) NOT NULL,
    region_key INTEGER NOT NULL,
    sales_channel VARCHAR(30) NOT NULL,
    payment_method VARCHAR(30) NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(14,2) NOT NULL CHECK (unit_price >= 0),
    discount_pct DECIMAL(5,2) NOT NULL CHECK (discount_pct BETWEEN 0 AND 100),
    revenue DECIMAL(14,2) NOT NULL,
    cost DECIMAL(14,2) NOT NULL,
    profit DECIMAL(14,2) NOT NULL,
    FOREIGN KEY (order_date) REFERENCES dim_date(date_key),
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
    FOREIGN KEY (region_key) REFERENCES dim_region(region_key)
);

CREATE INDEX idx_sales_date ON fact_sales(order_date);
CREATE INDEX idx_sales_product ON fact_sales(product_id);
CREATE INDEX idx_sales_customer ON fact_sales(customer_id);
