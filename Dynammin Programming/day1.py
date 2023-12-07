"""i = 0
j = 1
n = 4
if n==1:
    print(0)
elif n==2:
    print(0,1,sep="\n")
else:
    print(0,1,sep="\n")
    for _ in range(n-2):
        ans = i+j
        i = j
        j = ans
        print(ans)
"""
""""
#top down approach
a = 4
def fibtop(a,mem):
    if a == 1:
        return 0
    if a == 2:
        return 1
    if a not in mem:
        mem[a] = fibtop(a-1,mem)+fibtop(a-2,mem)
    return mem[a]
print(fibtop(a,{}))
"""



""""*************#Number factor i/p: 5 cond:1,3,4 ans:6****************
def num(a):
    if a in (0,1,2):
        return 1
    elif a == 3:
        return 2
    else:
        n1 = num(a-1)
        n2 = num(a-3)
        n3 = num(a-4)
        return n1+n2+n3
print(num(5))

def dpnum(a,dic):
    if a in (0,1,2):
        dic[0] = 1
        dic[1] = 1
        dic[2] = 1
        return 1
    elif a == 3:
        dic[3] = 2
        return 2
    else:
        if a not in dic:
            n1 = dpnum(a-1,dic)
            n2 = dpnum(a-3,dic)
            n3 = dpnum(a-4,dic)
            return n1+n2+n3
print(dpnum(5,{}))
"""


#***********************robbery problem************************
"""def rob(a,ind):
    if ind>=len(a):
        return 0
    steal = a[ind]+rob(a,ind+2)
    skip = rob(a,ind+1)
    return max(steal,skip)
#print(rob(a,0))"""

a = [6,7,1,30,8,2,4]
def robbu(a,ind):
    temp = [0]*(len(a)+2)
    for i in range(len(a)-1,-1,-1):
        temp[i] = max(a[i]+temp[i+2],temp[i+1])
    return(temp[0])
print(robbu(a,0))

#*******************
"""
s1 = 'table'
s2 = 'tgable'
def findMin(s1,s2,ind1,ind2):
    if ind1==len(s1):
        return len(s2)-ind2
    if ind2==len(s2):
        return len(s1)-ind1
    if s1[ind1]==s2[ind2]:
        return findMin(s1,s2,ind1+1,ind2+1)
    else:
        delop = 1+findMin(s1,s2,ind1,ind2+1)
        insop = 1+findMin(s1,s2,ind1+1,ind2)
        replaceop = 1+findMin(s1,s2,ind1+1,ind2+1)
        return min(delop,insop,replaceop)
print(findMin(s1,s2,0,0))
"""