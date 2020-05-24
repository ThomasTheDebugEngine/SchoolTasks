arr = []
userinput = 0

# for c in range[0,5]:
#   arr.append(input("enter number ")+ str(c+1) +": "))

# Asks for user input from us


def user_prompt(userinput):
    try:
        print("input here : ")
        userinput = int(input())
        arr.append(userinput)
    except:
        print("Input is not correct")
        exit()


# A for loop that asks for the input 5 times
for i in range(5):
    user_prompt(userinput)

solutionsarr = []

# Function that calculates the sum,the minimum and maximum of the array.And then we make an average by dividing the len of array and the sum of the array


def opeartions(arr):
    solutionsarr.append(sum(arr))
    solutionsarr.append(min(arr))
    solutionsarr.append(max(arr))
    solutionsarr.append(sum(arr)/len(arr))
    print(solutionsarr)


opeartions(arr)
