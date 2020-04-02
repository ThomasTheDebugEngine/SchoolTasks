import textwrap
from itertools import groupby

def program():
    #This part is getting the Inputs from the user.
    word = input("Please input a random letters: ")
    wordcount = len(word)
    number = int(input("Please input only int number: "))
    #This part is used to check if the 2nd input is divided by the 1st part equally, if not, it repeats.
    if (number > 0) and (int(wordcount) % number == 0):
        print("Inputs were received and returned Okay.")
    else:
        print("I am sorry but your inputs are invalid, Please try again :)")
        program()
    #This part divides the string into equal groups
    string = (textwrap.wrap(word, number))
    #This loop goes over the the divided groups
    for i in range(len(string)):
        new_string = ""
        #This loop reaaranges the divided groups and removes duplicates.
        for char in string[i]:
            if char not in new_string:
                new_string += char
        string[i] = new_string

    print(string)

program()
