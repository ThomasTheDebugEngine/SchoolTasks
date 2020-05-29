import sqlite3
from sqlite3 import Error
import time


class Database:
    def __init__(self):
        # connect to the databse and shop connection
        self.conn = self.connect("temporary.db")
        self.curs = self.conn.cursor()  # get database cursor object

    @property
    def conn(self):  # connection property
        return self._conn

    @conn.setter
    def conn(self, value):  # setter for connection property
        self._conn = value

    @property
    def curs(self):  # cursor property
        return self._curs

    @curs.setter
    def curs(self, value):  # setter for cursor property
        self._curs = value


    def connect(self, db_address):  # connect to database
        print("connecting to db...")

        try:
            connection = sqlite3.connect(db_address)
            print("connected to sqlite @ " + str(db_address))
        except Error as err:
            # return error if can't connect
            raise Exception("ERROR connecting to DB: " + str(err))

        return connection


    def create_shop_table(self):  # create the article table
        print("creating shop table...")

        self.curs.execute(
            '''CREATE TABLE shop (
                shop_id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT,
                items TEXT
            )'''
        )


    def create_item_table(self):  # create the comment table
        print("creating Item table...")

        self.curs.execute(
            '''CREATE TABLE items (
                item_id INTEGER PRIMARY KEY,
                barcode TEXT ,
                name TEXT,
                description TEXT,
                unit_price DECIMAL,
                timestamp,
                shop_id, 
                FOREIGN KEY (shop_id) 
                    REFERENCES shop(shop_id)
                    ON UPDATE NO ACTION
                    ON DELETE NO ACTION
            )'''
        )


    def create_component_table(self):  # create the comment table
        print("creating coponents table...")

        self.curs.execute(
            '''CREATE TABLE components (
                component_id INTEGER PRIMARY KEY,
                name TEXT,
                quantity DECIMAL,
                timestamp,
                item_id,
                FOREIGN KEY (item_id)
                    REFERENCES items(item_id)
                    ON UPDATE NO ACTION
                    ON DELETE NO ACTION
            )'''
        )


    def check_shop_table_exists(self):
        self.curs.execute(
            '''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='shop' ''')

        if self.curs.fetchone()[0] == 1:
            return True  # table exists
        else:
            return False  # table does not exist


    def print_all(self):
        self.curs.execute("SELECT * from shop")
        for row in self.curs:
            print(row)
        self.curs.execute("SELECT * from items")
        for row in self.curs:
            print(row)
        self.curs.execute("SELECT * from components")
        for row in self.curs:
            print(row)


    def check_item_table_exists(self):
        self.curs.execute(
            '''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='items' ''')
        if self.curs.fetchone()[0] == 1:
            return True  # table exists
        else:
            return False  # table does not exist


    def check_component_table_exists(self):
        self.curs.execute(
            '''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='components' ''')

        if self.curs.fetchone()[0] == 1:
            return True  # table exists
        else:
            return False  # table does not exist


    def create_shop(self, id, name, address, item_id):
        self.curs.execute('''INSERT INTO shop VALUES (?, ?, ?, ?)''', (id, name, address, item_id))
        self.conn.commit()
        


    def create_item(self, id, barcode, name, description, unit_price, shop_id, timestamp):
        self.curs.execute('''INSERT INTO items VALUES (?, ?, ?, ?, ?, ?,?)''',
                          (id, barcode, name, description, unit_price, timestamp, shop_id))
        self.conn.commit()


    def create_component(self, id, name, quanity, timestamp, item_id):
        self.curs.execute('''INSERT INTO components VALUES (?, ?, ?, ?, ?)''',
                          (id, name, quanity, timestamp, item_id))
        self.conn.commit()


    def database_main(self):  # main function for the database
        self.start_database()  # start the database


    def start_database(self):  # start the database
        if not self.check_shop_table_exists():
            self.create_shop_table()
        else:
            print("shop table already exists !")

        if not self.check_item_table_exists():
            self.create_item_table()
        else:
            print("items table already exists !")

        if not self.check_component_table_exists():
            self.create_component_table()
        else:
            print("components table already exists !")


    def modify_component_by_id(self, id, new_value):
        self.curs.execute("UPDATE components SET quantity={0} WHERE component_id={1}".format(str(new_value), id,))
        self.conn.commit()


    def delete_component_by_id(self, id):
        self.curs.execute("DELETE FROM components WHERE component_id={0}".format(id,))
        self.conn.commit()


db = Database()  # initialise database
db.database_main()  # start the database

db.create_shop(1, "IKI", "IKI Street 1", 5)
db.create_shop(2, "MAXIMA", "Kaunas, Maksima Street 2", 6)
db.create_item(3, 112233112233, "Zemaiciu bread", "", 1.55, time.time(), 1)
db.create_item(4, 33333222111, "Klaipeda Milk", "Milk from Klaipeda", 2.69, time.time(), 1)
db.create_item(12, 99898989898, "Aukstaiciu Bread", "", 1.65, time.time(), 2)
db.create_item(13, 99919191991, "Vilnius Milk", "Milk from Vinius", 2.99, time.time(), 2)

db.create_component(5, "Flour", 1.50, time.time(), 3)
db.create_component(6, "Water", 1.00, time.time(), 3)
db.create_component(7, "Milk", 1.00, time.time(), 4)

db.create_component(8, "Flour", 1.60, time.time(), 12)
db.create_component(9, "Water", 1.10, time.time(), 12)
db.create_component(10, "Milk", 1.10, time.time(), 13)

db.modify_component_by_id(6, 1.45)
db.delete_component_by_id(10)

db.print_all()
