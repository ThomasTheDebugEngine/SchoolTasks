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
            "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='shop' ")

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
        self.curs.execute(
            '''INSERT INTO shop VALUES (?, ?, ?, ?)''', (id, name, address, item_id))
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
# This is where we take a components quanitity by its ID .

    def modify_component_by_id(self, id, new_value):
        self.curs.execute("UPDATE components SET quantity={0} WHERE component_id={1}".format(
            str(new_value), id,))
        self.conn.commit()

    def delete_component_by_id(self, id):
        self.curs.execute(
            "DELETE FROM components WHERE component_id={0}".format(id,))
        self.conn.commit()
    # This function prints the items with the word in the parameter in it and we can use thisto do iet part

    def consists_word(self, name):
        self.curs.execute(
            '''SELECT * FROM items WHERE name LIKE '%?%''', (name))
        self.conn.commit()
    # We Quantify how many components have the same id as an item and then the print the length of te ampunt of rows in there

    def quanity_components(self, id):
        self.curs.execute(
            '''SELECT * FROM components WHERE item_id = '%?%''', (id))
        print(self.curs.len)

    # In this query we will baiscally select anything that has the word we put in parameters in the stores name and then display them
    def random_query(self, name):
        self.curs.execute(
            '''SELECT * FROM shop WHERE  name LIKE '%?%''', (name))
        for rows in self.curs:
            print(rows)
    # In here we get all the relative components from the Items

    def get_all_relative_components(self, first_item, second_item):
        self.curs.execute(
            "SELECT * FROM items WHERE item_id IN (?, ?)", (first_item, second_item,))
        items_arr = self.curs.fetchall()  # get the searched items from db

        item1_id = items_arr[0][0]  # extract the id from the items
        item2_id = items_arr[1][0]  # extract the id from the items

        self.curs.execute(
            "SELECT * FROM components WHERE item_id={0}".format(item1_id))
        item1_component_arr = self.curs.fetchall()

        self.curs.execute(
            "SELECT * FROM components WHERE item_id={0}".format(item2_id))
        item2_component_arr = self.curs.fetchall()

        commons_array = []  # array for common items
        for item1 in item1_component_arr:  # search component
            for item2 in item2_component_arr:
                if(item1[1] == item2[1]):
                    commons_array.append(item1)

        return commons_array


db = Database()  # initialise database
db.database_main()  # start the database

db.create_shop(1, "IKI", "IKI Street 1", 5)
db.create_shop(2, "MAXIMA", "Kaunas, Maksima Street 2", 6)
db.create_item(3, 112233112233, "Zemaiciu bread", "", 1.55, time.time(), 1)
db.create_item(4, 33333222111, "Klaipeda Milk",
               "Milk from Klaipeda", 2.69, time.time(), 1)
db.create_item(12, 99898989898, "Aukstaiciu Bread", "", 1.65, time.time(), 2)
db.create_item(13, 99919191991, "Vilnius Milk",
               "Milk from Vinius", 2.99, time.time(), 2)

db.create_component(5, "Flour", 1.50, time.time(), 3)
db.create_component(6, "Water", 1.00, time.time(), 3)
db.create_component(7, "Milk", 1.00, time.time(), 4)

db.create_component(8, "Flour", 1.60, time.time(), 12)
db.create_component(9, "Water", 1.10, time.time(), 12)
db.create_component(10, "Milk", 1.10, time.time(), 13)

db.modify_component_by_id(6, 1.45)
db.delete_component_by_id(10)

db.get_all_relative_components(3, 12)

db.count_components_of_items()

db.print_all()
