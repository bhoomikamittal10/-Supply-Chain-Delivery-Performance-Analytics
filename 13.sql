SELECT 
    suppliers.Supplier_Name,
    suppliers.Supplier_Rating,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN orders.Order_Status = 'Delivered' THEN 1 ELSE 0 END) AS delivered_orders,
    SUM(CASE WHEN orders.Order_Status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_orders
FROM orders
INNER JOIN suppliers ON orders.Supplier_ID = suppliers.Supplier_ID
GROUP BY suppliers.Supplier_Name, suppliers.Supplier_Rating
ORDER BY delivered_orders DESC;