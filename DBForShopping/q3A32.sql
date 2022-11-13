 SELECT CAST(os.size AS REAL)/CAST(COUNT(o.oid) AS REAL) average
 FROM Customers c, OrderSize os,Orders o 
 WHERE c.customer_id = o.customer_id  AND 
o.order_id = os.oid AND 
 customer_postal_code = (SELECT c.customer_postal_code FROM Customers c ORDER BY random() LIMIT 1);