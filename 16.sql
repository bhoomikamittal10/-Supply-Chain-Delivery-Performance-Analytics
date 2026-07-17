
USE SUPPLY_CHAIN;
SELECT 
    warehouses.Warehouse_City,
    ROUND(AVG(DATEDIFF(orders.Expected_Delivery_Date, orders.Order_Date)), 2) AS avg_lead_time_days
FROM orders
INNER JOIN warehouses ON orders.Warehouse_ID = warehouses.Warehouse_ID
GROUP BY warehouses.Warehouse_City
ORDER BY avg_lead_time_days DESC;