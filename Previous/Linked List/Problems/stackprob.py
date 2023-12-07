
a = [15,5,18,19,19,2,4,17,7,16,14,5,19,2,5,7,5,12,15,1,7,8,2,12,12,4,19,18,1,11,2,16,16,0,7,7,15]
b = [3,5,14,19,19,19,18,1,16,17,6,0,13,19,7,1,1,12,5,6,11,3,19,14,5,7,3,18,14,10,13,10,15,19,9,14,11,0,7,7,17,6,8,10,5,7,3,7,19,8]
maxSum = 64
#a = [0,12,12,19]
#b = [15,6,1,18,7,15,5,14,14,1,12,15,8,16,14,2,14,9,13,12,18,19,3,18]
a = a[::-1]
b = b[::-1]
#maxSum =81
l2= []
l1 = []
sum1,sum2=0,0
count1,count2,fcount = 0,0,0
while sum1<maxSum:
    if a:
        sum1 = sum1 + a.pop()
        count1 = count1 + 1
    else:
        break
while sum2<maxSum:
    if b:
        sum2 = sum2 + b.pop()
        count2 = count2 + 1
    else:
        break

if count1>count2:
    ftemp = count1
ftemp = count2


print(ftemp)
