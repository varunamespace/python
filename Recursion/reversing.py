l = [1,2]
l[0], l[1] = l[1], l[0]
print(l)
def reverse(l,start,stop):
    if start != stop and start < stop:
        l[start], l[stop] = l[stop] , l[start]
        reverse(l,start+1,stop-1)

l = [1,2,3,4,5]
reverse(l,0,len(l)-1)
print(l)

