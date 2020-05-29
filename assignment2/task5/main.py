import json
import sys
import os

class Item:
    # Constructor
    def __init__(self, name, quantity=1, price=10):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.total_price = quantity * price

    # Method to get total_price
    def get_total_price(self):
        return self.quantity * self.price

    # Method to get all info of the objects
    def full_info(self):
        return self.name + " " + str(self.price) + " " + str(self.quantity) + " " + str(self.get_total_price())

    # Method to show everything as a dictionary
    def to_dict(self):
        return self.__dict__


class Food(Item):
    # since "Food" class is inheriting from the "Item" class there is not need to rewrite the constructor.
    # I only copied the method of full_info and applied adjustment to it.
    def full_info(self):
        return " Food " + self.name + " " + str(self.price) + " " + str(self.quantity) + " " + str(self.get_total_price())


class Drink(Item):
    # since "Drink" class is inheriting from the "Item" class there is not need to rewrite the constructor.
    # I only copied the method of full_info and applied adjustment to it.
    def full_info(self):
        return " Drink " + self.name + " " + str(self.price) + " " + str(self.quantity) + " " + str(self.get_total_price())


class Customer:

    # Constructor with private name and class variable.
    identifier = 0

    def __init__(self, name, price, itemname, quantity):
        Customer.identifier += 1
        self.__name = name
        self.identifier = Customer.identifier
        self.Food = Food(itemname, price, quantity)

    # Decorator for our constructor class
    @property
    def name(self):
        return self.__name

    # a setter to the constructor
    @name.setter
    def setter(self, name, price, quantity, itemname):
        self.__name = name
        self.Food = Food(itemname, price, quantity)

    # our identifier which counts the Customer class
    def get_identifier(self):
        return self.identifier

    # collects the objects Identifier together with his full name.
    def full_name(self):
        return str(self.identifier) + " " + self.__name + self.Food.full_info()

    @staticmethod
    def export_to_json():
        savepath = 'C:/pythexample/'
        filename = input("Enter the file name: ")
        completename = os.path.join(savepath, filename+".json")
        file1 = open(completename, "w")
        file1.write(str(c1_dict))
        file1.close()

# Creating 3 objects (Customers)
c1 = Customer("Jonas Jonaitis", 1, "1.3", "Bread")
c2 = Customer("Djonas Vikas", 1, "1.4", "Pencils")
c3 = Customer("Baulius Vondalius", 1, "1.3", "Bread")

# Priniting the full name of the objects together with their Identifier (number).
print(c1.full_name())
print(c2.full_name())
print(c3.full_name())

c1_dict = {
    "identifier": c1.identifier,
    "name": c1.name,
    "items_list": {"Food": "Bread",
                   "Quantity": "1",
                   "Price": "1.3",
                   "Drink": "Coca-Cola",
                   "Quantity": "2",
                   "Price": "3"}}

c1.export_to_json()