#a=[1,3,5,9,11]
#a = a[::-1]
#26152
#[6320, 12040, 18060, 5328, 6660, 4032, 4704, 5376, 6048, 6720]
a = [6320,6020,6098,1332,7263,672,9472,2838,3401,9494]

#a = [1,2,3,4,5]
#a = [8979,4570,6436,5083,7780,3269,5400,7579,2324,2116]
print(a)
l = []
res,rev,count,norev=0,0,0,0
for i in range(len(a)):
    if a[i] < a[(len(a)-1)-i]:
        norev = norev + 1
    else:
        rev = rev + 1
print(rev,norev)
if rev > norev:
    a = a[::-1]
elif rev == norev:
    if a[0] < a[-1]:
        a = a[::-1]

mini = min(a)
print(a)
for i in range(len(a)):
    val = a.pop(0)
    count = count + 1
    if mini>=val:
        mini = val
    res = mini*count
    l.append(res)
print(max(l))
