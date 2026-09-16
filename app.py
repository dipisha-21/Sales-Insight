from flask import Flask, render_template_string
import csv
import io
import random
from datetime import date, timedelta

app = Flask(__name__)

PRODUCTS = [
    ("Laptop Pro", "Technology", 85000, 65000),
    ("Wireless Mouse", "Technology", 1800, 900),
    ("Office Chair", "Furniture", 14500, 9500),
    ("Notebook Pack", "Office Supplies", 450, 220),
    ("Monitor 27", "Technology", 24000, 17500),
]
REGIONS = ["South", "West", "North", "East"]


def make_sample(n=2000):
    rng = random.Random(42)
    start = date(2025, 1, 1)
    rows = []
    for i in range(n):
        name, category, price, cost = rng.choice(PRODUCTS)
        qty = rng.randint(1, 5)
        discount = rng.choice([0, 0, 5, 10, 15])
        revenue = qty * price * (1 - discount / 100)
        total_cost = qty * cost
        rows.append({
            "date": start + timedelta(days=rng.randint(0, 365)),
            "product": name,
            "category": category,
            "region": rng.choice(REGIONS),
            "quantity": qty,
            "revenue": revenue,
            "profit": revenue - total_cost,
        })
    return rows


ROWS = make_sample()


@app.route("/")
def home():
    revenue = sum(r["revenue"] for r in ROWS)
    profit = sum(r["profit"] for r in ROWS)
    orders = len(ROWS)
    margin = 100 * profit / revenue if revenue else 0
    aov = revenue / orders if orders else 0
    regions = []
    for region in REGIONS:
        rr = [r for r in ROWS if r["region"] == region]
        regions.append((region, sum(r["revenue"] for r in rr), sum(r["profit"] for r in rr)))
    regions.sort(key=lambda x: x[1], reverse=True)

    return render_template_string('''
<!doctype html><html><head><title>Sales Insight Dashboard</title>
<style>body{font-family:Arial;max-width:1100px;margin:40px auto;padding:0 20px;background:#f5f7fb;color:#20242b}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.card{background:#fff;padding:22px;border-radius:14px;box-shadow:0 4px 18px #0001}.metric{font-size:28px;font-weight:700;margin-top:8px}table{width:100%;border-collapse:collapse;margin-top:16px}th,td{padding:12px;border-bottom:1px solid #ddd;text-align:left}small{color:#667}</style></head><body>
<h1>Sales Insight Dashboard</h1><p>Live portfolio demo of the SQL + Power BI + DAX analytics project using reproducible synthetic transactions.</p>
<div class="grid"><div class="card"><small>Total Revenue</small><div class="metric">₹{{'{:,.0f}'.format(revenue)}}</div></div><div class="card"><small>Total Profit</small><div class="metric">₹{{'{:,.0f}'.format(profit)}}</div></div><div class="card"><small>Profit Margin</small><div class="metric">{{'{:.1f}'.format(margin)}}%</div></div><div class="card"><small>Average Order Value</small><div class="metric">₹{{'{:,.0f}'.format(aov)}}</div></div></div>
<div class="card" style="margin-top:18px"><h2>Regional Performance</h2><table><tr><th>Region</th><th>Revenue</th><th>Profit</th></tr>{% for name,rev,prof in regions %}<tr><td>{{name}}</td><td>₹{{'{:,.0f}'.format(rev)}}</td><td>₹{{'{:,.0f}'.format(prof)}}</td></tr>{% endfor %}</table></div>
</body></html>''', revenue=revenue, profit=profit, margin=margin, aov=aov, regions=regions)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
