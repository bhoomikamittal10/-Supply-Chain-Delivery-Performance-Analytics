# 📦 Supply Chain & Delivery Performance Analytics

An end-to-end analysis of a 52,000+ order supply chain dataset, taken through the full analyst workflow: **SQL → Python → Power BI Dashboard**, with a strong focus on data quality, multi-table relational analysis, and statistical validation.

---

## 📌 Business Question

> Which warehouses, suppliers, and product categories are driving delivery delays and order cancellations — and where should the business focus improvement efforts?

---

## 🗂️ Dataset

A normalized, 5-table relational dataset (simulated to reflect real-world enterprise data quality challenges):

| Table | Rows | Description |
|---|---|---|
| `orders` | 52,780 | Core transactional data — dates, status, quantities |
| `products` | 48 | Product catalog with category and pricing |
| `warehouses` | 8 | Warehouse locations across major Indian cities |
| `suppliers` | 12 | Supplier details with ratings and regions |
| `inventory` | 270 | Product × Warehouse stock levels and reorder thresholds |

**Intentional data quality issues** (to reflect real enterprise systems): inconsistent date formats, missing values (~43% of orders pending/cancelled/delayed), inconsistent text casing, and ~1,500+ duplicate records — all identified and resolved as part of the analysis.

---

## 🔧 Tools & Workflow

| Stage | Tool | What Was Done |
|---|---|---|
| 1. Data Modeling & Cleaning | **MySQL** | Multi-table schema design, missing value/duplicate detection, deduplication using window functions |
| 2. Relational Analysis | **MySQL** | Multi-table JOINs, CASE WHEN logic, subqueries, GROUP BY aggregations |
| 3. Statistical Analysis | **Python (pandas, scipy, seaborn)** | Time-series trends, category-level analysis, Pearson correlation testing |
| 4. Dashboard | **Power BI** | Interactive KPI dashboard with category and trend visualizations |

---

## 📊 Key Insights

1. **Data quality baseline established.** 43% of orders had no actual delivery date (reflecting in-transit, cancelled, or delayed status) — this was explicitly accounted for in all delay-based calculations to avoid skewed averages.

2. **Delivery delays are systemic, not warehouse-specific.** Average delivery delay was remarkably consistent across all 8 warehouses (1.96–2.03 days), suggesting the root cause is likely a company-wide process (e.g., last-mile logistics) rather than any single facility's operations.

3. **Supplier rating does not predict reliability.** A Pearson correlation test between supplier rating and cancellation rate returned a near-zero correlation (r = 0.156, p = 0.629 — not statistically significant). Notably, the supplier with the highest order volume (Krishna Traders, 4,407 orders) had a below-average rating of 3.0, indicating that rating alone is an unreliable signal of operational performance.

4. **Beverages has the highest cancellation rate.** At 15.04%, Beverages ranked highest among all 10 categories — about 1.15 percentage points above the lowest (Household, 13.89%) — a modest but consistent gap worth investigating (e.g., perishability or delivery time sensitivity).

5. **35.25% of inventory value is tied up in low-turnover ("dead") stock.** Using a stock-to-order ratio to flag the top 20% highest-risk products, ₹1.06 Cr out of ₹3.01 Cr total inventory value was identified as slow-moving — representing a significant working-capital optimization opportunity.

6. **Demand is stable with no strong seasonality.** A 3-month moving average forecast projected ~2,285 orders for the following month, consistent with actual monthly volumes ranging 2,130–2,353 — indicating predictable demand that supports steady inventory and staffing planning rather than reactive scaling.

---

## 💡 Recommendations

- **Investigate last-mile logistics company-wide** rather than targeting specific warehouses, since delay patterns are consistent across all locations.
- **Do not use supplier rating as a sole vendor selection criterion** — pair it with operational metrics like on-time delivery rate and cancellation rate, which showed no meaningful relationship with rating in this dataset.
- **Review Beverages category fulfillment process** specifically, given its consistently elevated cancellation rate relative to other categories.
- **Prioritize clearance/reorder-reduction strategies for the flagged dead-stock segment** (₹1.06 Cr, 35.25% of inventory value) to free up working capital.
- **Use the stable demand forecast (~2,285 orders/month) as a planning baseline**, adjusting only when actual volumes deviate meaningfully from this range.

---

## 📁 Repository Structure

```
supply-chain-analytics/
├── data/
│   ├── orders.csv
│   ├── products.csv
│   ├── warehouses.csv
│   ├── suppliers.csv
│   └── inventory.csv
├── sql/
│   └── queries.sql              # Schema creation, cleaning, JOIN-based analysis
├── python/
│   └── analysis.py              # pandas merge, time-series, correlation testing
├── powerbi/
│   ├── dashboard.pbix
│   └── dashboard_screenshot.png
└── README.md
```

---

## 🖼️ Dashboard Preview



## 🛠️ Skills Demonstrated

**SQL**: Multi-table JOINs (INNER JOIN across 4 tables), CASE WHEN conditional aggregation, subqueries, window functions (ROW_NUMBER for deduplication), GROUP BY/HAVING, data quality auditing (IS NULL, duplicate detection)

**Python**: pandas (merge, groupby, agg with custom lambda functions), datetime handling with mixed formats, scipy.stats (Pearson correlation, hypothesis testing), seaborn/matplotlib visualization, moving-average demand forecasting, inventory valuation and dead-stock risk scoring (quantile-based thresholding)

**Supply Chain Analytics**: Lead time analysis, dead stock / inventory risk identification, demand forecasting (moving average), supplier reliability scoring

**Power BI**: KPI cards, interactive filtering (slicers), category and time-series visualizations, data type transformation

**Data Quality**: Missing value identification and handling, duplicate detection and removal using two independent methods (exact-match and composite-key matching), documentation of data limitations

---

## 🛠️ Skills Demonstrated

SQL: Multi-table JOINs (INNER JOIN across 4 tables), CASE WHEN conditional aggregation, subqueries, window functions (ROW_NUMBER for deduplication), GROUP BY/HAVING, data quality auditing (IS NULL, duplicate detection)

Python: pandas (merge, groupby, agg with custom lambda functions), datetime handling with mixed formats, scipy.stats (Pearson correlation, hypothesis testing), seaborn/matplotlib visualization, moving-average demand forecasting, inventory valuation and dead-stock risk scoring (quantile-based thresholding)

Supply Chain Analytics: Lead time analysis, dead stock / inventory risk identification, demand forecasting (moving average), supplier reliability scoring

Power BI: KPI cards, interactive filtering (slicers), category and time-series visualizations, data type transformation

Data Quality: Missing value identification and handling, duplicate detection and removal using two independent methods (exact-match and composite-key matching), documentation of data limitations

