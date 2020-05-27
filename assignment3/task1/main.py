import sqlite3
from sqlite3 import Error
import time


class Database:
    def __init__(self):
        # connect to the databse and store connection
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

    def create_store_table(self):  # create the article table
        print("creating store table...")
        self.curs.execute(
            '''CREATE TABLE store (
                store_id INTEGER PRIMARY KEY, 
                name TEXT, 
                address TEXT, 
                items TEXT, 
                item_id,
                FOREIGN KEY (item_id)
                    REFRENCES items (item_id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
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
                store_id,
                timestamp,
                FOREIGN KEY (store_id)
                    REFERENCES store (store_id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
            )'''
        )

    def create_component_table(self):  # create the comment table
        print("creating coponents table...")
        self.curs.execute(
            '''CREATE TABLE component (
                component_id INTEGER PRIMARY KEY,
                name TEXT,
                quantity DECIMAL,
                timestamp,
                item_id,
                FOREIGN KEY (store_id)
                    REFERENCES articles (store_id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
            )'''
        )

    def database_main(self):  # main function for the database
        self.start_database()  # start the databse
