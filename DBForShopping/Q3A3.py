import sqlite3
import matplotlib.pyplot as plt
import numpy as np
from time import time 

connection = None
cursor = None

def connect(path):

    global connection,cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    connection.commit()
    return

def Uninformed():

    global connection,cursor

    cursor.execute(' PRAGMA foreign_keys = false ')
    cursor.execute(' PRAGMA automatic_index=false')

    cursor.execute("CREATE TABLE 'CustomersNew' (	'customer_id'	TEXT,	 'customer_postal_code'	INTEGER);       ")
    cursor.execute("CREATE TABLE 'Order_itemsNew' (	'order_id'	TEXT,	'order_item_id'	INTEGER,	'product_id'	INTEGER,	'seller_id'	INTEGER);     ")
    cursor.execute("CREATE TABLE 'OrdersNew' ('order_id'	TEXT,'customer_id'	INTEGER); ")  
    cursor.execute("CREATE TABLE 'SellersNew' ('seller_id'	TEXT,'seller_postal_code'	INTEGER);        ")

    cursor.execute("INSERT INTO CustomersNew SELECT customer_id, customer_postal_code FROM Customers ")
    cursor.execute("INSERT INTO Order_itemsNew SELECT order_id, order_item_id, product_id, seller_id FROM Order_items ")
    cursor.execute("INSERT INTO OrdersNew SELECT order_id, customer_id FROM Orders ")
    cursor.execute("INSERT INTO SellersNew SELECT seller_id, seller_postal_code FROM Sellers ")

    cursor.execute("ALTER TABLE Customers RENAME TO CustomersOriginal")
    cursor.execute("ALTER TABLE Order_items RENAME TO Order_itemsOriginal")
    cursor.execute("ALTER TABLE Orders RENAME TO OrdersOriginal")
    cursor.execute("ALTER TABLE Sellers RENAME TO SellersOriginal")

    cursor.execute("ALTER TABLE CustomersNew RENAME TO Customers")
    cursor.execute("ALTER TABLE Order_itemsNew RENAME TO Order_items")
    cursor.execute("ALTER TABLE OrdersNew RENAME TO Orders")
    cursor.execute("ALTER TABLE SellersNew RENAME TO Sellers")

    connection.commit()
    return

def SelfOptimized():

    global connection,cursor

    cursor.execute(' PRAGMA foreign_keys=true')
    cursor.execute(' PRAGMA automatic_index=true')

    cursor.execute("DROP TABLE Customers")
    cursor.execute("DROP TABLE Order_items")
    cursor.execute("DROP TABLE Orders")
    cursor.execute("DROP TABLE Sellers")

    cursor.execute("ALTER TABLE CustomersOriginal RENAME TO Customers")
    cursor.execute("ALTER TABLE Order_itemsOriginal RENAME TO Order_items")
    cursor.execute("ALTER TABLE OrdersOriginal RENAME TO Orders")
    cursor.execute("ALTER TABLE SellersOriginal RENAME TO Sellers")
   
    connection.commit()
    return

def UserOptimized():
    global connection,cursor

    cursor.execute(' PRAGMA foreign_keys=true')
    cursor.execute(' PRAGMA automatic_index=true')

    cursor.execute("DROP INDEX IF EXISTS customer_id_index_cus")
    cursor.execute("DROP INDEX IF EXISTS customer_id_index_ord")
    cursor.execute("DROP INDEX IF EXISTS customer_id_index_ord_items")

    cursor.execute("CREATE INDEX customer_id_index_cus ON Customers(customer_postal_code,customer_id)")
    cursor.execute("CREATE INDEX customer_id_index_ord ON Orders(customer_id)")
    cursor.execute("CREATE INDEX customer_id_index_ord_items ON Order_items (order_id)")

    connection.commit()
    return
    
def print_50times_result():

    import time

    start_time=time.time()

    for i in range(50):
        cursor.execute(""" SELECT COUNT( o.order_id ) ,AVG( itemss.number_of_items )
FROM Customers c, Orders o,
(
SELECT order_id,count(*) as number_of_items 
FROM Order_items oi
GROUP BY oi.order_id)
AS itemss
WHERE c.customer_id = o.customer_id  
AND  customer_postal_code = ( 
SELECT c.customer_postal_code 
FROM Customers c ORDER BY random() LIMIT 1)
AND o.order_id = itemss.order_id;""" )

    end_time=time.time()

    connection.commit()

    avg_time =  (end_time - start_time) / 50 *1000

    return avg_time

def times(db_path):
    
    global connection, cursor
    
    connect(db_path)
    Uninformed()
    Uninformed_avg_time = print_50times_result()
    connection.close()

    connect(db_path)
    SelfOptimized()
    SelfOptimized_avg_time = print_50times_result()
    connection.close()

    connect(db_path)
    UserOptimized()
    UserOptimized_avg_time = print_50times_result()
    connection.close()

    return [Uninformed_avg_time, SelfOptimized_avg_time, UserOptimized_avg_time]

def bar_chart(one, two, three, four, five, six, seven, eight, nine):

    labels = ['SmallDB', 'MediumDB', 'LargeDB']
    
    uninformed = [one, four, seven]
    self_optimized = [two, five, eight]
    user_optimized = [three, six, nine]

    width = 0.4

    fig, ax = plt.subplots()

    uninformed=np.array(uninformed)
    self_optimized=np.array(self_optimized)
    user_optimized=np.array(user_optimized)

    ax.bar(labels, uninformed, width, label="Uninformed")
    ax.bar(labels, self_optimized, width, bottom = uninformed, label="Self Optimized")
    ax.bar(labels, user_optimized, width, bottom=uninformed+self_optimized, label="User Optimized")

    ax.set_ylabel("Query runtime in milliseconds")
    ax.set_title("Query_3")
    ax.legend()

    tl = "Q3A3"

    path = './{}chart.png'.format(tl)
    plt.savefig(path)
    print('Chart saved to file {}'.format(path))

    plt.close()
    return

    #print("          ")

    #print("Small Uninformed: " + str(one))
    #print("Small Self-optimized: " + str(two))
    #print("Small User-optimized: " + str(three))

    #print("------------------------------------")

    #print("Medium Uninformed: " + str(four))
    #print("Medium Self-optimized: " + str(five))
    #print("Medium User-optimized: " + str(six))

    #print("------------------------------------")

    #print("Large Uninformed: " + str(seven))
    #print("Large Self-optimized: " + str(eight))
    #print("Large User-optimized: " + str(nine))

    #print("          ")

    #return


def main():

    #small database
    db_path_Small = "./A3Small.db"
    small_db_results = times(db_path_Small)

    #medium database
    db_path_Medium = "./A3Medium.db"
    medium_db_results = times(db_path_Medium)
    
    #large database
    db_path_Large= "./A3Large.db"
    large_db_results = times(db_path_Large)

    one = small_db_results[0]
    two = small_db_results[1]
    three = small_db_results[2]

    four = medium_db_results[0]
    five = medium_db_results[1]
    six = medium_db_results[2]

    seven = large_db_results[0]
    eight = large_db_results[1]
    nine = large_db_results[2]

    bar_chart(one, two, three, four, five, six, seven, eight, nine)

  
if __name__ == "__main__":
    main()