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
    
    def remove_item(self, type, index):
        if(int(index) > -1):    
            if(type == "food"):
                if(len(self.__foodArr) > 0):
                    print("removed " + str(self.__foodArr[int(index)]))
                    del self.__foodArr[int(index)]
                
                else:
                    print("Error removing item")
            
            elif(type == "drink"):
                if(len(self.__foodArr) > 0):
                    print("removed " + str(self.__drinkArr[int(index)]))
                    del self.__foodArr[int(index)]
                
                else:
                    print("Error removing item")


        else:
            print("please enter a valid index")
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
# flow controller

c4 = customer("putin", ["food","bread", 1, 2])
# add customers like above and save to array below
customerArr = [c4]

count = 0
def inputInterface(editMode):
    global customerArr
    global count

    if(editMode == "add"):
        count = count + 1
        
        itemType = input("input item type, [food] or [drink]: ")
        itemName = input("input item name: ")
        itemQty = input("input quantity: ")
        itemPrice = input("input price: ")

        itemArr = [itemType , itemName, itemQty, itemPrice]
        
        if(itemType == "food"):
            itemObj = food("food", itemName, itemQty, itemPrice)
            customerArr[0].add_item("object", itemObj, -1)
        
        elif(itemType == "drink"):
            itemObj = drink("drink" , itemName, itemQty, itemPrice)
            customerArr[0].add_item("object", itemObj, -1)
        
        else:
            print ("please enter a valid option, [food] or [drink]")
            inputInterface(editMode)


    elif(editMode == "remove" and count > 0):
        count = count - 1

        idx = input("input the index you want to remove: ")
        
        if(len(idx) == 0):
            print("please enter a value")
            inputInterface(editMode)

        elif(idx.isdigit()):
            customerArr[0].remove_item("food", idx) # remove selected indexes from selected customers

        else:
            print("please enter a number")
            inputInterface(editMode)


    elif(editMode == "remove" and not count > 0):
        print("cannot remove before adding a customer")

#------------------------------------------------------------------------------
# loop program prompt

def startAgain():
    inputMore = input("input more ? [y]es or [n]o: ")

    if(inputMore == "y"):
        inputInterface("add", -1)

    elif(inputMore == "n"):
        return 0
    
    else:
        print("please enter a valid option")
        startAgain()

#------------------------------------------------------------------------------
# program start


# add and then remove (manual flow set)
inputInterface("add") 
inputInterface("remove")

startAgain()