SELECT Order_ID, COUNT(*) AS how_many_times
FROM orders
GROUP BY Order_ID
HAVING COUNT(*) > 1;