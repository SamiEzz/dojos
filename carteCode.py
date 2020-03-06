from random import randint
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print(list[9])
isInA = 1
isInB = 2
isInC = 3


def randomise(_list):
    randList = _list
    for i in range(5):
        offset1 = randint(0, 12)
        offset2 = randint(offset1, 17)
        offset3 = randint(offset2, 20)
        randList = randList[offset2:offset3] + randList[offset3:21] + \
            randList[0:offset1]+randList[offset1:offset2]
    return randList


def findIt(a, b, c, chosenNum):
    for i in range(len(a)):
        if(a[i] == chosedNum):
            return isInA
        if(b[i] == chosedNum):
            return isInB
        if(c[i] == chosedNum):
            return isInC


def reDms(a, b, c, whereItIs):
    if(whereItIs == isInA):
        k = b+a+c
    if(whereItIs == isInB):
        k = c+b+a
    if(whereItIs == isInC):
        k = a+c+b
    return k


def reDivise(a, b, c, randomList):
    a = []
    b = []
    c = []
    for i in range(7):
        a.append(randomList[i*3])
        b.append(randomList[i*3+1])
        c.append(randomList[i*3+2])


while(1):
    randomList = randomise(list)
    chosedNum = randint(0, 20)
    #chosedNum = 0
    print(chosedNum)
    for k in range(4):
        a = []
        b = []
        c = []
        for i in range(7):
            a.append(randomList[i*3])
            b.append(randomList[i*3+1])
            c.append(randomList[i*3+2])
        isInPile = findIt(a, b, c, chosedNum)
        randomList = reDms(a, b, c, isInPile)
        reDivise(a, b, c, randomList)

    print(randomList[10])
    print("___________")
