arr = [10,65,2,75,150]

# for c in range[0,5]:
#   arr.append(input("enter number ")+ str(c+1) +": "))

newarr=[]
for x in range(0,len(arr)):
    if int(arr[x]) >= 10 and int(arr[x]) <= 100:
        newarr.append(arr[x])

solutionsarr = []
def opeartions (newarr):
    solutionsarr.append(sum(newarr))
    solutionsarr.append(min(newarr))
    solutionsarr.append(max(newarr))
    solutionsarr.append(sum(newarr)/len(newarr))
    print(solutionsarr)

opeartions(newarr)