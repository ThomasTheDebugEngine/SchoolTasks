import sys

def program():
    #This part is getting the Inputs from the user.
    word = input("Please input a random letters: ")
    wordCount = len(word)
    number = int(input("Please input only int number: "))

    #This part check if the entered string can be equally divided into the entered number, if not it quits the program.(couldn't find Restart command)
    if (int(number) > 0) and (wordCount % number == 0):
        print("Inputs were received and returned Okay.")
    else:
        print("I am sorry but your inputs are invalid, Please try again :)")
        program()

    # needs Improvement but it kinda works.
    result = "".join(sorted(set(word), key=word.index))
    out = [(result[i:i+number]) for i in range(0, len(result), number)]
    print(out)

program()