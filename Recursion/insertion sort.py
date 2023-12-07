#Insertion Sort
def insert(alist):
    for i in range(1,len(alist)):
        cur = alist[i]
        j = i
        while alist[j-1] > cur:
            alist[j] = alist[j-1]
            j -= 1
        alist[j] = cur
    return alist

l=[1,3,2,4,6,5]
print(l)
l1 = insert(l)
print(l1)



