class customer:
    def __init__(self, name, cartArr):
        self.__name = name
        self.__cartArr = cartArr
        self.__foodArr = []
        self.__drinkArr = []

        self.add_item("list", -1, self.__cartArr)
        

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

#------------------------------------------------------------------------------
# arr input props and setters

    @property
    def cartArr(self):
        return self.__cartArr


    @cartArr.setter
    def cartArr(self, cartArr):
        self.__cartArr = cartArr

#------------------------------------------------------------------------------
# obj input props and setters

    @property
    def foodArr(self):
        return self.__foodArr

    @foodArr.setter
    def foodArr(self, foodArr):
        self.__foodArr = foodArr

    
    @property
    def drinkArr(self):
        return self.__drinkArr

    @drinkArr.setter
    def drinkArr(self, drinkArr):
        self.__drinkArr = drinkArr
    
#------------------------------------------------------------------------------
# methods

    def add_item(self, mode, inputObj, inputList):
        if(mode == "list"):
            if(inputList[0] == "food"):
                slicedList = inputList[1:]
                self.__foodArr.append(slicedList)
                print(self.__foodArr) # for testing
            
            elif(inputList[0] == "drink"):
                slicedList = inputList[1:]
                self.__drinkArr.append(slicedList)
                print(self.__foodArr) # for testing


        elif(mode == "object"):
            if(inputObj.type == "food"):
                slicedList = [inputObj.name, inputObj.quantity, inputObj.price]
                self.__foodArr.append(slicedList)
                print(self.__foodArr) # for testing

            elif(inputObj.type == "drink"):
                slicedList = [inputObj.name, inputObj.quantity, inputObj.price]
                self.__drinkArr.append(slicedList)
                print(self.__drinkArr) # for testing

            return 0
    
    def remove_item(self, inputObj):
        return 0

    def outputResult(self):
        print("name: " + self.__name + ", cart items: " + str(self.cartArr))


#------------------------------------------------------------------------------
# aux classes

class food:
    def __init__(self, type, foodName, quantity, price):
        self.type = type
        self.name = foodName
        self.quantity = quantity
        self.price = price


class drink:
    def __init__(self, type, drinkName, quantity, price):
        self.type = type
        self.name = drinkName
        self.quantity = quantity
        self.price = price

#------------------------------------------------------------------------------
# testing

# cart = foodArr + drinkArr
# print(tstfood.returnList())
# c2 = customer("bond" , food("butter", 2, 1))

# c2.add_item(food("butter23", 2, 1))

# foodItem = food("bread" , 1, 4)

# tstfood = ["bread", 2, 4]

# c1 = customer("wick", tstfood)
# c1.outputResult()

#------------------------------------------------------------------------------
# flow splitter

def inputInterface():
    itemType = input("input item type, [food] or [drink]: ")
    itemName = input("input item name: ")
    itemQty = input("input quantity: ")
    itemPrice = input("input price: ")

    itemArr = [itemType , itemName, itemQty, itemPrice]
    
    if(itemType == "food"):
        itemObj = food("food", itemName, itemQty, itemPrice)
        app(itemArr, itemObj)
    
    elif(itemType == "drink"):
        itemObj = drink("drink" , itemName, itemQty, itemPrice)
        app(itemArr, itemObj)
    
    else:
        print ("please enter a valid option, [food] or [drink]")
        inputInterface()

#------------------------------------------------------------------------------
# flow unifier

# ! issue with scoping on constructor (doesn't recognise c3 object in else)

c4 = customer("putin", ["food","bread", 1, 2])
def app(inputArr, inputObj):
    global c4

    c4.add_item("object", inputObj, -1)
    
    #c4.outputResult()

#------------------------------------------------------------------------------
# loop program prompt

def startAgain():
    inputMore = input("input more ? [y]es or [n]o: ")

    if(inputMore == "y"):
        inputInterface()

    elif(inputMore == "n"):
        return 0
    
    else:
        print("please enter a valid option")
        startAgain()


inputInterface()
startAgain()