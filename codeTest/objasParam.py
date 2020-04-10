class customer:
    def __init__(self, name , cartArr):
        self.__name = name
        self.__cartArr = cartArr

    @property
    def name(self):
        return self.__name

    @property
    def cartArr(self):
        return self.__cartArr

    @name.setter
    def name(self, name):
        self.__name = name

    @cartArr.setter
    def cartArr(self, cartArr):
        self.__cartArr = cartArr

    def outputResult(self):
        print("name: " + self.__name + ", cart items: " + str(self.cartArr))



foodArr = ["bread", 1, 2.5]
drinkArr = ["cola", 2, 3.5]

cart = foodArr + drinkArr

c1 = customer("wick", cart)
c1.outputResult()