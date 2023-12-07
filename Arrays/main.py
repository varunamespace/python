"""
#MOVE ZEROS
def movezeros(a):
    a = list(a)
    count = 0
    for i in a:
        if i == 0:
            a.remove(i)
            count+=1
    for i in range(count):
        a.append(0)
    print(a)

def newmovezeros(a):
    j = 0
    for i in a:
        if i!=0:
            a[j] = i
            j+=1
    for i in range(j,len(a)):
        a[i] = 0
    print(a)

a = [0,1,0,3,12]
newmovezeros(a)

"""
import math

"""

#VALID MOUNTAIN ARRAYS
l = [1,2,3,4,5,4,3,2,1]
start = 0
end = len(l)-1
while l[start] < l[start+1]:
    start = start + 1
for i in range(end,start,-1):
    if l[end] < l[end-1]:
        res = "yes"
    else:
        res = "no"
print(res)
"""
"""
#Longest Substring without Repeating Characters
#i/p:abcabcbb
#o/p:3
a = "abcabcbb"
def longsub(a):
    r,l,ans=0,0,0
    dict = {}
    while r<len(a) and l<len(a):
        temp = a[r]
        if(temp in dict):
            l = max(l,dict[temp]+1)
        dict[temp] = r
        ans = max(ans,r-l+1)
        r+=1
    print(ans)
longsub(a)
"""
"""
#First and Last Position of element in sorted list
def binarysearch(list,tar):
    left = 0
    right = len(list)-1
    while left<=right:
        mid = (left + right)//2
        if list[mid] == tar:
            return mid
        elif tar < list[mid]:
            right = mid - 1
        elif tar > list[mid]:
            left = mid + 1
        else:
            return -1
a = [1,2,3,4,4,4,4,4,4]
print(binarysearch(a,4))
"""
"""
def firstoccurance(a,tar):
    left = 0
    right = len(a)-1
    while left<=right:
        mid = (left+right)//2
        if a[mid]==tar:
            if a[mid-1]!=tar and mid == 0:
                return mid
            right = mid - 1
        elif a[mid]<tar:
            left = mid  + 1
        else:
            right = mid - 1
def lastoccurance(a,tar):
    left = 0
    right = len(a)-1
    while left<=right:
        mid = (left+right)//2
        if a[mid]==tar:
            if a[mid+1]!=tar or mid==len(a)-1:
                return mid
            left = mid + 1
        elif a[mid] < tar:
            left = mid + 1
        else:
            right = mid - 1
a = [11,11,11,14,15]
print(lastoccurance(a,11))
print(firstoccurance(a,11))
"""
"""
def binarysearch(a,tar):
    l = 0
    r = len(a)-1
    while l<=r:
        mid = (l+r)//2
        if a[mid]==tar:
            r = mid
        elif tar>a[mid]:
            l = mid+1
        elif tar<a[mid]:
            r = mid-1
        else:
            return -1
a = [1,2,3,4,4,5,6,9,12,43]
a = [1,1,0,0,0,0,0,0]
print(binarysearch(a,0))
"""
"""
#Find the duplicate in array
#a=[1,2,3,2]
a = [6,6,6,6]
def find(a):
    d = {}
    for i in a:
        if i in d:
            return i
        d[i] = 1
print(find(a))
"""
"""
#SLIDING WINDOW

a = [1,3,4,7,8,9]
def slid(a,s):
    val,maxval=0,0
    for i in range(s):
        val = val + a[i]
    maxval =val
    for i in range(len(a)-s):
        val = val - a[i] + a[i+s]
        maxval = max(maxval,val)
    return maxval
print(slid(a,2))
"""
"""
#count prime numbers

n = 10
l=[True]*n
#print(l)
l[0]=l[1]=False
print(l)
for i in range(2,int(math.ceil(math.sqrt(n)))):
    if l[i]:
        for i in range(i*i,n,i):
            l[i] = False
print(l)
"""
"""
#single number
a = [2,2,1,1,4]
def find1duplicate(a):
    b = set()
    got = sum(a)
    for i in a:
        b.add(i)
    exp = 2*(sum(b))
    return exp-got
print(find1duplicate(a))
"""
"""
#two elements appear once and other element appear twice
a = [1,2,1,3,2,5]
#a = [-1,0]
#a = [0,1,1,2]
def simplenumber(a):
    b = set()
    for i in a:
        b.add(i)
    val = 2*(sum(b))-sum(a)
    dict = {}
    for i in b:
        if i in dict:
            return (i,dict[i])
        dict[val-i] = i
print(simplenumber(a))
"""
"""
#cyclic sort
a = [1,2,3,5,4]
def cyclicsort(a):
    i = 0
    while i<len(a):
        if a[i]!=i+1:
            a[a[i]-1],a[i] = a[i],a[a[i]-1]
        i = i + 1
cyclicsort(a)
print(a)
"""
"""
a = '110101'
b = '110001'
def addbinary(a,b):
    i = len(a)-1
    j = len(b)-1
    carry = 0
    res = []
    while i>=0 or j>=0 or carry:
        total = carry
        if i >=0:
            total = total + int(i)
            i = i - 1
        if j >=0:
            total = total + int(j)
            j-=1
        res.append(str(total%2))
        carry = carry//2
    return ''.join(reversed(res))
print(addbinary(a,b))
"""
"""
#Majority Element
a = [1,1,2,3,2,2,2]
def majorityelement(a):
    d = {}
    for i in a:
        d[i] = d.get(i,0)
        d[i] = d[i] + 1
    for i in d:
        if d[i]>len(a)//2:
            return i
print(majorityelement(a))
"""
s = 'abaacad'
t = 'aab'
def minsubwindow(s,t):
    strlen = len(s)
    tarlen = len(t)
    strhash = {}
    tarhash =  {}
    if strhash < tarhash:
        return ""
    for i in t:
        if tarhash.get(i) is None:
            tarhash[i] = 0
        tarhash[i] = tarhash[i] + 1
    left,count,minlen = 0,0,0
    for right in range(0,strlen):
        if strhash.get(s[right]) is None:
            strhash[s[right]] = 0
        strhash[s[right]] = strhash[s[right]] + 1
        if strhash.get(s[right])<=tarhash.get(s[right]):
            count+=1
        if count == tarlen:
            strhash[s[left]] = strhash[s[left]] - 1
            while strhash.get(s[left])<=tarhash.get(s[left]):
                continue

print(minsubwindow(s,t))
























