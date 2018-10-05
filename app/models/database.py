import os
import psycopg2
from psycopg2 import  Error

# connection = psycopg2.connect(user="postgres",
#                             password="root123",
#                             host="127.0.0.1",
#                               port="5432",
#                             database="challengethree")

# cursor =  connection.cursor()



class DatabaseConnection:   
    def __init__(self):     
        try:
            if os.getenv("two") == "one":
                self.connection = psycopg2.connect(user="huthjazzsyrtes",
                                                   password="26322b4349b6b5afae9aac7a2aed4e193f26b7f56b12758d8e53057843fedb88",
                                                   host="ec2-50-17-225-140.compute-1.amazonaws.com",
                                                   port="5432",
                                                   database="d9qjbmi8scereg")
                                                
                self.connection.autocommit = True
                self.cursor = self.connection.cursor()
            else:
                self.connection = psycopg2.connect(user="postgres",
                                                   password="root123",
                                                   host="127.0.0.1",
                                                   port="5432",
                                                   database="challengethree")
                self.connection.autocommit = True
                self.cursor = self.connection.cursor()

            #print PostgreSQl properties
            #print (self.connection.get_dsn_parameters(), "\n")

            #print postgres version
            # self.cursor.execute("SELECT version();")
            # self.record = self.cursor.fetchone()
            #print("You are connected to - ", self.record, "\n")


        except(Exception, psycopg2.DatabaseError) as error:
                print ("Error while conneccting to PostgreSQL", error)
            




    def create_user_table(self):
        self.user_table = (
            "CREATE TABLE IF NOT EXISTS users (userId serial primary key, username varchar(50) not null, password varchar not null )")
        self.cursor.execute(self.user_table)
        

    def create_menu_list(self):
        self.menu_table = (
            "CREATE TABLE IF NOT EXISTS menu (menuId serial primary key, menuItem varchar(50) not null, menuDescription varchar(500)not null )")
        self.cursor.execute(self.menu_table)

    def create_order_list(self):
        self.order_table = ("CREATE TABLE IF NOT EXISTS orders (orderId serial primary key,userId int not null, FOREIGN KEY(userId) REFERENCES users(userId), menuId int not null, FOREIGN KEY(menuId) REFERENCES menu(menuId))")
        self.cursor.execute(self.order_table)
        
    def drop_data_from_orders_table(self, drop_orders):
        self.drop_orders = "DROP TABLE orders"
        self.cursor.execute(drop_orders)
