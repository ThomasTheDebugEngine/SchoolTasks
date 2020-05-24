arr = []
userinput = 10
# for c in range[0,5]:
#   arr.append(input("enter number ")+ str(c+1) +": "))
newarr = []

# Function to ask for users input


def user_prompt(userinput):
    try:
        print("input here : ")
        userinput = int(input())
        arr.append(userinput)
    except:  # Catches for an error so if the user enters a string or something instead of a number this is throw an error.
        print("Input is not correct")
        exit()


# A for loop to ask for the input 5 times
for i in range(5):
    user_prompt(userinput)

# A function to basically filter out the stuff above 10 and less than 100
for x in range(0, len(arr)):
    if int(arr[x]) >= 10 and int(arr[x]) <= 100:
        newarr.append(arr[x])

solutionsarr = []


# Function that calculates the sum,the minimum and maximum of the array.And then we make an average by dividing the len of array and the sum of the array
def opeartions(newarr):
    solutionsarr.append(sum(newarr))
    solutionsarr.append(min(newarr))
    solutionsarr.append(max(newarr))
    solutionsarr.append(sum(newarr)/len(newarr))
    print(solutionsarr)


opeartions(newarr)

# The decorator function that we call on the function to perform the function


def decoratorfunction(solutionsarr, userinput):
    for y in range(0, len(solutionsarr)):
        solutionsarr[y] -= userinput
    print(solutionsarr)


decoratorfunction(solutionsarr, userinput)
