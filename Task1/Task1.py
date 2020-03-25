def splitN(word):
    return list(word)

word = input("Enter a word or a sentence: ")

def splitOptionA(checkA):
    return list(checkA)

checkA = input("Enter letters / numbers: ")

def splitOptionB(checkB):
    return list(checkB)

checkB = input("Enter different letters / numbers: ")

print(splitN(word))
print(splitOptionA(checkA))
print(splitOptionB(checkA))

countA = 0
countB = 0
for x in word:
    for y in checkA:
        if x == y:
            countA = countA + 1


for x in word:
    for y in checkB:
        if x == y:
            countB = countB + 1

print(countA)
print(countB)

sum = countA - countB
print(sum)