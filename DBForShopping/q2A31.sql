 CREATE VIEW OrderSize (oid,size)
 AS
 SELECT o.order_id,oi.order_item_id
 FROM Orders o, Order_items oi
 WHERE o.order_id = oi.order_id

 