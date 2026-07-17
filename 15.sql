SELECT 
    products.Product_Name,
    products.Category,
    warehouses.Warehouse_City,
    inventory.Stock_Quantity,
    COUNT(orders.Order_ID) AS times_ordered
FROM inventory
INNER JOIN products ON inventory.Product_ID = products.Product_ID
INNER JOIN warehouses ON inventory.Warehouse_ID = warehouses.Warehouse_ID
LEFT JOIN orders ON inventory.Product_ID = orders.Product_ID AND inventory.Warehouse_ID = orders.Warehouse_ID
GROUP BY products.Product_Name, products.Category, warehouses.Warehouse_City, inventory.Stock_Quantity
ORDER BY inventory.Stock_Quantity DESC
LIMIT 20;