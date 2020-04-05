class Customer:

    #Constructor with private name and class variable.
    identifier = 0
    def __init__(self, name):
        Customer.identifier += 1
        self.__name = name
        self.identifier = Customer.identifier

    #Decorator for our constructor class
    @property
    def name(self):
        return self.__name

    #a setter to the constructor
    @name.setter
    def name(self, name):
        self.__name = name

    #our identifier which counts the Customer class
    def get_identifier(self):
        return self.identifier

    #collects the objects Identifier together with his full name.
    def full_name(self):
        return str(self.identifier) + " " + self.__name

#Creating 3 objects (Customers)
c1 = Customer("Jonas Jonaitis")
c2 = Customer("Petras Petraitis")
c3 = Customer("Lukas Lukauskas")

#Printing the total Objects which are 3.
print(Customer.identifier)

#Printing each objects identifier depends on their creation.
print(c1.get_identifier())
print(c2.get_identifier())
print(c3.get_identifier())

#Printing the total of the objects again.
print(Customer.identifier)

#Priniting the full name of the objects together with their Identifier (number).
print(c1.full_name())
print(c2.full_name())
print(c3.full_name())