def reverse(l,start,stop):
    if start < stop:
        l[start] , l[stop] = l[stop], l[start]
        reverse(l,start+1,stop-1)
    return l


l=[1,2,3,4,5]
print(reverse(l,0,len(l)-1))
print(len(l))





