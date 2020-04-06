arr = []
userinput = 0

# for c in range[0,5]:
#   arr.append(input("enter number ")+ str(c+1) +": "))


def user_prompt(userinput):
    print("input here : ")
    userinput = int(input())
    arr.append(userinput)


for i in range(5):
    user_prompt(userinput)

solutionsarr = []


def opeartions(arr):
    solutionsarr.append(sum(arr))
    solutionsarr.append(min(arr))
    solutionsarr.append(max(arr))
    solutionsarr.append(sum(arr)/len(arr))
    print(solutionsarr)


opeartions(arr)
