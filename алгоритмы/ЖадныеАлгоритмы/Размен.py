def change(money):
    numCoins = 0
    coins = []
    while money > 0:
        if money >= 10:
            money = money - 10
            coins.append(10)
        elif money >= 5:
            money = money - 5
            coins.append(5)
        else:
            money = money - 1
            coins.append(1)
            numCoins += 1
    return coins
def num_change(arr):
    i = arr.count(10)
    j = arr.count(5)
    k = arr.count(1)
    sttr = []
    contic = []
    for l in range(i+1, 0, -1):
        string = ''
        for m in range(j+1, 0, -1):
            string = '10 ' * (l - 1)
            string += '5 '*(m-1)
            num_one = a - (10*(l-1))-(5*(m-1))
            string += '1 '*num_one
            cont = (m-1)+(l-1)+num_one
            sttr.append(string)
            contic.append(cont)
        j += 2

    print(len(contic))
    for i in range(0, len(sttr)):
        print(contic[i], sttr[i].strip())


a = int(input())
c=change(a)
num_change(c)