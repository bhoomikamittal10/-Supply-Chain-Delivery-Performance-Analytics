import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Saari CSVs load karo
orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')
warehouses = pd.read_csv('warehouses.csv')
suppliers = pd.read_csv('suppliers.csv')
inventory = pd.read_csv('inventory.csv')

# print(orders.shape)
# print(orders.head())

# print("Before removing duplicates:", orders.shape)

# orders = orders.drop_duplicates()

# print("After removing duplicates:", orders.shape)


merged = orders.merge(products, on='Product_ID', how='inner')
merged = merged.merge(warehouses, on='Warehouse_ID', how='inner')
merged = merged.merge(suppliers, on='Supplier_ID', how='inner')

print(merged.shape)
print(merged.head())

merged['Order_Date'] = pd.to_datetime(merged['Order_Date'], format='mixed')
merged['Order_Month'] = merged['Order_Date'].dt.to_period('M')

monthly_trend = merged.groupby('Order_Month').size()
print(monthly_trend)

category_stats = merged.groupby('Category').agg(
    total_orders=('Order_ID', 'count'),
    cancelled=('Order_Status', lambda x: (x == 'Cancelled').sum())
)
category_stats['cancellation_rate_pct'] = round((category_stats['cancelled'] / category_stats['total_orders']) * 100, 2)
category_stats = category_stats.sort_values('cancellation_rate_pct', ascending=False)
print(category_stats)

supplier_stats = merged.groupby('Supplier_Name').agg(
    avg_rating=('Supplier_Rating', 'mean'),
    cancellation_rate=('Order_Status', lambda x: (x == 'Cancelled').mean() * 100)
)

correlation, p_value = stats.pearsonr(supplier_stats['avg_rating'], supplier_stats['cancellation_rate'])
print(f"Correlation: {correlation}")
print(f"P-value: {p_value}")

# plt.figure(figsize=(12,5))
# monthly_trend.plot(kind='line', marker='o')
# plt.title('Monthly Order Trend')
# plt.xlabel('Month')
# plt.ylabel('Number of Orders')¸
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(10,6))
# sns.barplot(x=category_stats.index, y=category_stats['cancellation_rate_pct'], palette='Reds_r')
# plt.title('Cancellation Rate by Category')
# plt.xlabel('Category')
# plt.ylabel('Cancellation Rate (%)')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

merged.to_csv('merged_supply_chain_data.csv', index=False)
print("Saved successfully!")
# Demand Forecasting - Simple Moving Average
monthly_orders = merged.groupby('Order_Month').size().reset_index(name='order_count')
monthly_orders = monthly_orders.sort_values('Order_Month')

# 3-month moving average
monthly_orders['moving_avg_3m'] = monthly_orders['order_count'].rolling(window=3).mean()

# # Next month ka simple forecast = last 3 months ka average
# next_month_forecast = monthly_orders['order_count'].tail(3).mean()

# print(monthly_orders.tail(6))
# print(f"\nForecasted orders for next month: {round(next_month_forecast, 0)}")

# Dead Stock Impact Analysis
inventory_merged = inventory.merge(products, on='Product_ID')
inventory_merged['stock_value'] = inventory_merged['Stock_Quantity'] * inventory_merged['Unit_Price_INR']

total_inventory_value = inventory_merged['stock_value'].sum()

# Order count per product-warehouse combo nikaalo
merged_orders_count = merged.groupby(['Product_ID', 'Warehouse_ID']).size().reset_index(name='order_count')
inventory_with_demand = inventory_merged.merge(merged_orders_count, on=['Product_ID', 'Warehouse_ID'], how='left')
inventory_with_demand['order_count'] = inventory_with_demand['order_count'].fillna(0)

# Stock-to-order ratio nikaalo
inventory_with_demand['stock_to_order_ratio'] = inventory_with_demand['Stock_Quantity'] / (inventory_with_demand['order_count'] + 1)

# Top 20% highest ratio = dead stock (potential risk)
threshold = inventory_with_demand['stock_to_order_ratio'].quantile(0.80)
dead_stock = inventory_with_demand[inventory_with_demand['stock_to_order_ratio'] >= threshold]

dead_stock_value = dead_stock['stock_value'].sum()
dead_stock_pct_of_total = round((dead_stock_value / total_inventory_value) * 100, 2)

print(f"Total Inventory Value: Rs.{total_inventory_value:,.0f}")
print(f"Dead Stock Value (top 20% risk): Rs.{dead_stock_value:,.0f}")
print(f"Dead Stock as % of Total Inventory: {dead_stock_pct_of_total}%")