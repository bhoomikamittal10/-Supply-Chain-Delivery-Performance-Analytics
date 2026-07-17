SELECT 
    warehouses.Warehouse_City,
    ROUND(AVG(DATEDIFF(orders.Actual_Delivery_Date, orders.Expected_Delivery_Date)), 2) AS avg_delay_days
FROM orders
INNER JOIN warehouses ON orders.Warehouse_ID = warehouses.Warehouse_ID
WHERE orders.Order_Status = 'Delivered'
GROUP BY warehouses.Warehouse_City
ORDER BY avg_delay_days DESC;