SELECT 
    warehouses.Warehouse_City,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN orders.Order_Status = 'Delayed' THEN 1 ELSE 0 END) AS delayed_orders
FROM orders
INNER JOIN warehouses ON orders.Warehouse_ID = warehouses.Warehouse_ID
GROUP BY warehouses.Warehouse_City
ORDER BY delayed_orders DESC;