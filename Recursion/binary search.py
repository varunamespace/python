def binary_search(data,target,low,high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif target <= data[mid]:
            return binary_search(data, target, low , mid-1)
        else:
            return binary_search(data, target, mid+1, high)


l1 = [1,2,3,4,5,6,7,8,9,10]
high = len(l1)
print(binary_search(l1,10,0,len(l1)-1))




