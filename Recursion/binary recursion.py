def binary_sum(l,start,stop):
    if start >= stop:
        return 0
    elif start = stop -1:
        return l[start]
    else:
        mid = start + stop
        return binary_sum(l,start,mid) + binary_sum(l,mid+stop)
