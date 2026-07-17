-- SELECT orders.Order_ID, products.Product_Name
-- FROM orders
-- INNER JOIN products ON orders.Product_ID = products.Product_ID
-- LIMIT 10;

SELECT 
    orders.Order_ID,
    products.Product_Name,
    products.Category,
    warehouses.Warehouse_City,
    suppliers.Supplier_Name,
    orders.Order_Status,
    orders.Quantity_Ordered
FROM orders
INNER JOIN products ON orders.Product_ID = products.Product_ID
INNER JOIN warehouses ON orders.Warehouse_ID = warehouses.Warehouse_ID
INNER JOIN suppliers ON orders.Supplier_ID = suppliers.Supplier_ID
LIMIT 15;