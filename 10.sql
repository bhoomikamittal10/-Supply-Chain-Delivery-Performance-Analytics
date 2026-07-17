-- CREATE TEMPORARY TABLE temp_duplicates AS
-- SELECT Order_ID, Product_ID, Warehouse_ID, Supplier_ID, Order_Date,
--        Expected_Delivery_Date, Actual_Delivery_Date, Order_Status, Quantity_Ordered,
--        ROW_NUMBER() OVER (PARTITION BY Order_ID ORDER BY Order_ID) AS row_num
-- FROM orders;

SET SQL_SAFE_UPDATES = 0;

-- DELETE FROM orders
-- WHERE (Order_ID, Product_ID, Warehouse_ID, Supplier_ID, Order_Date, Order_Status, Quantity_Ordered) IN (
--     SELECT Order_ID, Product_ID, Warehouse_ID, Supplier_ID, Order_Date, Order_Status, Quantity_Ordered
--     FROM temp_duplicates
--     WHERE row_num > 1
-- );

SELECT COUNT(*) FROM orders;
