def splitN(n):
    return list(n)

n = input("Enter a word or a sentence: ")

def splitOptionA(a):
    return list(a)

a = input("Enter letters / numbers: ")

def splitOptionB(b):
    return list(b)

b = input("Enter different letters / numbers: ")

print(splitN(n))
print(splitOptionA(a))
print(splitOptionB(b))

count = 0
lengthA = str(range(a))

for a in lengthA:
    if a == lengthA:
        count = count + 1
    print(count)