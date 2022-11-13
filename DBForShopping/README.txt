GROUP NUMBER: 53

GROUP MEMBER CCID'S: 

1) oglinzan
2) xiangtia
3) wchang1

Our group only had 3 memebers work on the assignment

!! We declare that we did not collaborate with anyone outside our own group in this assignment !!

Query #1: 
For this query, we chose to index the customer_id column in both the Customers and Orders table.
This was done because in our 'WHERE' clause we search for a match between these two columns in the 
Customers and Orders table. Indexing allows for a much more efficient search. 

Query #2: 
Since the query 2 is an extension of query 1, and so the index search to match Customers and Orders are same as
query 1 do.


Query #3: 
For this query, we chose to create index for customer_postal_code and customer_id in both the Customers, Orders, and Order_items since we
wanna find out the total number of items divided by total number of Orders of that random postal code.


Query #4: 
For this query, we chose the index on seller_id and seller_postal_code columns on Sellers and order_id, seller_id columns and Order_items
tables. By matching with the seller_id, the code runtime will be more efficient. The rest of the index can also reduce the search time.