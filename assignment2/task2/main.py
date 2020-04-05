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

i1 = Item("Carrots")
i2 = Item("Milk", 2, 1.5)
i3 = Item("Bread", price=0.5)

print(i1.full_info())
print(i2.full_info())
print(i3.full_info())

print(i1.to_dict())
print(i2.to_dict())
print(i3.to_dict())