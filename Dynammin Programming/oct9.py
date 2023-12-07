"""##Best time to buy and sell a product for maximum profit
a = [7,1,5,3,6,4]
mini = 1000
fin = 0
for i in a:
    if i < mini:
        mini = i
    fin = max(i-mini,fin)
print(fin)
"""
"""
######Climbing Stairs#####
n = 6
opt = 1,2
l = []
def climb(n):
    if n ==1:
        return 1
    elif n ==2:
        return 2
    else:
        res = climb(n-1)+climb(n-2)
        return res
"""
"""
########Coin Change########
a = 11
coins = [1,1,2]
c = 0
def change(a,c):
    ind = (len(c)-1)
    r = a
    count = 0
    while 1:
        if r>=c[ind]:
            r = r-(c[ind])
            count = count + 1
        else:
            ind = ind -1
        if r == 0:
            break
    return count
print(change(a,coins))
"""
am = [1,2,5]
amount = 11
a = [float('inf')]*(amount+1)
print(a)
for i in a:



