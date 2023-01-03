from random import choice
def new_board():
    global a
    a = [[2 for i in range(8)] for j in range(8)]

def getIndexPositions(listOfElements, element):
    global indexPosList
    indexPosList = []
    indexPos = 0
    while True:
        try:
            indexPos = listOfElements.index(element, indexPos)
            indexPosList.append(indexPos)
            indexPos += 1
        except ValueError as e:
            break
    return indexPosList

def choose_ran():
    global count
    listof = []
    global i
    global j
    for idx in range(len(a)):
        if 2 in a[idx]:
            listof.append(idx)
    i = choice(listof)
    j = choice(getIndexPositions(a[i], 2))
    if a[i][j] != 1 and a[i][j] !=0:
        a[i][j] = 1
        count=count+1

def rows():
    for l in range(len(a[i])):
        if a[i][l] == 1:
            continue
        else:
            a[i][l] = 0
def cols():
    for l in range(len(a[i])):
        if a[l][j] == 1:
            continue
        else:
            a[l][j] = 0

def before_up():
    t=1
    n=1
    if i>j:
        for g in range(j):
            if a[i-t][j-t] != 1:
                a[i-t][j-t] = 0
                if t == j:
                    break
                t+=1
    else:
        for h in range(i):
            if a[i-n][j-n] != 1:
                a[i-n][j-n] = 0
                if i == n:
                    break
                n+=1
    q=1
    w=1
    if i>j:
        for g in range(7-i):
            if a[i+q][j+q] != 1:
                a[i+q][j+q] = 0
            if i == 7:
                break
            q+=1
    else:
        for g in range(7-j):
            if a[i+w][j+w] != 1:
                a[i+w][j+w] = 0
            if j == 7:
                break
            w+=1

def sth():
    for g in range(9):
        if i+g in range(8) and j-g in range(8):
            if a[i+g][j-g] != 1:
                a[i+g][j-g] = 0
    for g in range(9):
        if i-g in range(8) and j+g in range(8):
            if a[i-g][j+g] != 1:
                a[i-g][j+g] = 0

gh = []
user_request = 1 #int(input('how many do you want? '))
while len(gh) < user_request:
    count = 0
    new_board()
    while True:
        try:
            choose_ran()
        except Exception as e:
            if count == 8:
                for jk in a:
                    print(jk)
                if a not in gh:
                    gh.append(a)
                print(len(gh))
            break
        rows()
        cols()
        before_up()
        sth()