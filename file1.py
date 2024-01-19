import mysql.connector
class ShoppingSystem:
    def __init__(self) :
        self.connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pythontest"

        )
        self.cursor=self.connection.cursor()
    def add_products(self,name,price,quantity):
        sql="INSERT INTO products(name,price,quantity) VALUES (%s,%s,%s)"
        values=(name,price,quantity) 
        self.cursor.execute(sql,values)
        self.connection.commit() 
    def view_products(self):
        self.cursor.execute("SELECT * FROM products")
        products=self.cursor.fetchall()
        for product in products:
            print(product)

    def close_connection(self):
        self.connection.close()

s=ShoppingSystem()
#s.add_products("laptop",1000,5)
s.add_products("headphones",2399,1)
s.view_products()
