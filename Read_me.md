# Cash Flow Forecast & Runway Model — SaaS Startup (Series A)

A 24-month cash flow forecast and runway analysis for a fictional B2B SaaS startup ("LumaFlow"), built in Excel and analyzed with Python. This project demonstrates how I help founders answer the question that matters most: **"How long will our money last?"**

> All data in this project is fictional and built for demonstration purposes.

---

## The Scenario

LumaFlow is a Series A B2B SaaS company that recently raised $12M. It's growing fast (8% monthly MRR growth) but burning cash aggressively to capture market share. The model answers:

- How many months of runway remain at the current burn rate?
- When does the company run out of cash?
- How does aggressive hiring accelerate the burn?

---

## Key Findings

- **Starting cash:** $11.5M
- **Monthly net burn:** ~$580K, growing to ~$780K as headcount scales
- **Runway:** ~14 months — cash goes negative around **March 2027**
- **Insight:** The simple "cash ÷ average burn" rule overstates runway by ~3 months because burn is accelerating. The dynamic model catches what the rule of thumb misses.

---

## What's Inside

| File | Description |
|------|-------------|
| `Cash_Flow_Forecast_Runway_Tech_startup.xlsx` | The full model — assumptions, 24-month forecast, runway analysis, and dashboard |
| `cash_flow_analysis.py` | Python script that reads the model and auto-generates charts |
| `cash_balance_chart.png` | Cash balance over time (the runway curve) |
| `mrr_chart.png` | MRR growth |
| `revenue_costs_burn_chart.png` | Revenue vs. costs vs. net burn |

---

## How It Works

The Excel model is fully driven by an editable **Assumptions** tab — change a growth rate or hiring pace, and the entire forecast updates. The Python script then reads the model and regenerates all charts automatically, so reporting doesn't require manual rework.

**Tools:** Excel · Python · pandas · matplotlib

---

## Approach

The model separates inputs from calculations (no hardcoded numbers in formulas), follows standard financial modeling conventions, and is structured so the same framework can be adapted to any early-stage SaaS company by swapping in their actual numbers.
## Running the Analysis

```bash
python cash_flow_analysis.py
```

The script reads the Excel model, extracts the forecast rows, and regenerates all charts. Example of how it locates the runway automatically:

```python
import pandas as pd
import matplotlib.pyplot as plt

EXCEL_PATH = r"Cash_FLow_Forecast_Runway_Tech_startup.xlsx"

xls = pd.ExcelFile(EXCEL_PATH)
print("Sheets found:", xls.sheet_names)

# Read the Monthly_Forecast sheet without assuming clean headers
df = pd.read_excel(EXCEL_PATH, sheet_name="Monthly_Forecast", header=None)

# Preview the first rows to understand the structure
print(df.head(20))
print("---")
print("Dimensions (rows, columns):", df.shape)

# Extract key rows (excluding column 0, which holds the text labels)
dates = df.iloc[0, 1:].values            # Row 0: dates
mrr = df.iloc[3, 1:].values              # Row 3: MRR
total_revenue = df.iloc[12, 1:].values   # Row 12: Total Revenue
total_costs = df.iloc[13, 1:].values     # Row 13: Total Costs
net_burn = df.iloc[14, 1:].values        # Row 14: Net Burn
cash_balance = df.iloc[15, 1:].values    # Row 15: Cash Balance

# Verify the extraction
print("Dates:", dates[:3], "...")
print("Cash Balance start:", cash_balance[0], "| end:", cash_balance[-1])
print("Net Burn start:", net_burn[0])

# === CHART 1: Cash Balance Over Time ===
plt.figure(figsize=(10, 6))
plt.plot(dates, cash_balance, color="#1f3a93", linewidth=2.5, marker="o", markersize=3)

# Horizontal line at zero (the critical point)
plt.axhline(y=0, color="red", linestyle="--", linewidth=1, alpha=0.7)

# Titles and labels
plt.title("Cash Balance Over Time", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Cash Balance ($)")

# Format the Y axis in millions for readability
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x/1e6:.0f}M"))

plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save as image
plt.savefig("cash_balance_chart.png", dpi=150)
print("Chart saved: cash_balance_chart.png")

# === CHART 2: MRR Over Time ===
plt.figure(figsize=(10, 6))
plt.plot(dates, mrr, color="#16a085", linewidth=2.5, marker="o", markersize=3)

plt.title("MRR Over Time", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("MRR ($)")
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x/1e3:.0f}K"))

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("mrr_chart.png", dpi=150)
print("Chart saved: mrr_chart.png")

# === CHART 3: Revenue vs Costs vs Net Burn ===
plt.figure(figsize=(10, 6))
plt.plot(dates, total_revenue, color="#16a085", linewidth=2.5, label="Total Revenue")
plt.plot(dates, total_costs, color="#f39c12", linewidth=2.5, label="Total Costs")
plt.plot(dates, net_burn, color="#c0392b", linewidth=2.5, label="Net Burn")

plt.axhline(y=0, color="gray", linestyle="--", linewidth=1, alpha=0.5)

plt.title("Revenue vs Costs vs Net Burn", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x/1e6:.1f}M"))

plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("revenue_costs_burn_chart.png", dpi=150)
print("Chart saved: revenue_costs_burn_chart.png")
```