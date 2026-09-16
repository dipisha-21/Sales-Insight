"""Generate 60,000 reproducible synthetic sales transactions for portfolio use."""
from pathlib import Path
import csv
import random
from datetime import date, timedelta

SEED = 42
ROWS = 60_000
random.seed(SEED)

PRODUCTS = [
    ("P001", "Laptop Pro", "Technology", "Computers", 85000, 65000),
    ("P002", "Wireless Mouse", "Technology", "Accessories", 1800, 900),
    ("P003", "Mechanical Keyboard", "Technology", "Accessories", 5200, 3100),
    ("P004", "Office Chair", "Furniture", "Chairs", 14500, 9500),
    ("P005", "Standing Desk", "Furniture", "Tables", 28000, 19000),
    ("P006", "Notebook Pack", "Office Supplies", "Stationery", 450, 220),
    ("P007", "Printer", "Technology", "Printers", 16500, 12000),
    ("P008", "Bookshelf", "Furniture", "Storage", 11000, 7200),
    ("P009", "Monitor 27", "Technology", "Displays", 24000, 17500),
    ("P010", "Desk Lamp", "Furniture", "Accessories", 2200, 1200),
]
REGIONS = {
    "South": ["Karnataka", "Telangana", "Tamil Nadu"],
    "West": ["Maharashtra", "Gujarat", "Goa"],
    "North": ["Delhi", "Uttar Pradesh", "Punjab"],
    "East": ["West Bengal", "Odisha", "Jharkhand"],
}
CHANNELS = ["Online", "Retail", "Partner"]
PAYMENTS = ["UPI", "Card", "Net Banking", "Cash"]
START = date(2023, 1, 1)


def generate(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["order_id", "order_date", "customer_id", "product_id", "product_name",
              "category", "sub_category", "region", "state", "sales_channel",
              "payment_method", "quantity", "unit_price", "discount_pct",
              "revenue", "cost", "profit"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for i in range(1, ROWS + 1):
            product_id, name, category, subcategory, price, unit_cost = random.choice(PRODUCTS)
            region = random.choice(list(REGIONS))
            state = random.choice(REGIONS[region])
            quantity = random.randint(1, 5)
            discount = random.choice([0, 0, 0, 5, 10, 15, 20])
            revenue = round(quantity * price * (1 - discount / 100), 2)
            cost = round(quantity * unit_cost, 2)
            writer.writerow({
                "order_id": f"ORD{i:06d}",
                "order_date": (START + timedelta(days=random.randint(0, 1095))).isoformat(),
                "customer_id": f"C{random.randint(1, 5000):05d}",
                "product_id": product_id,
                "product_name": name,
                "category": category,
                "sub_category": subcategory,
                "region": region,
                "state": state,
                "sales_channel": random.choice(CHANNELS),
                "payment_method": random.choice(PAYMENTS),
                "quantity": quantity,
                "unit_price": price,
                "discount_pct": discount,
                "revenue": revenue,
                "cost": cost,
                "profit": round(revenue - cost, 2),
            })


if __name__ == "__main__":
    output = Path(__file__).resolve().parents[1] / "data" / "generated_sales.csv"
    generate(output)
    print(f"Generated {ROWS:,} rows at {output}")
