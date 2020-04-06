class Item:
    #Constructor
    def __init__(self, name, quantity=1, price=10):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.total_price = quantity * price

    #Method to get total_price
    def get_total_price(self):
        return self.quantity * self.price

    #Method to get all info of the objects
    def full_info(self):
        return self.name + " " + str(self.price) + " " + str(self.quantity) + " " + str(self.get_total_price())

    #Method to show everything as a dictionary
    def to_dict(self):
        return self.__dict__

class Food(Item):

    def __init__(self, name, quantity=1, price=10):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.total_price = quantity * price

    def full_info(self):
        return "Food " + self.name + " " + str(self.price) + " " + str(self.quantity) + " " + str(self.get_total_price())

class Drink(Item):

    def __init__(self, name, quantity=1, price=10):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.total_price = quantity * price

    def full_info(self):
        return "Drink " + self.name + " " + str(self.price) + " " + str(self.quantity) + " " + str(self.get_total_price())

f1 = Food("Bread", 2, 1.3)
f2 = Food("Butter", 1, 1.3)

d1 = Drink("CocaCola", 3, 1.7)
d2 = Drink("Sprite", 2, 1.7)

print(f1.full_info())
print(f2.full_info())
print(d1.full_info())
print(d2.full_info())