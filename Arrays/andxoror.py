a = [9,6,3,5,2]
def andXorOr(a):
    stack = []
    def findminandmax(a, length):
        min1 = min(a[0], a[1])
        min2 = max(a[0], a[1])
        for i in range(2, length + 1):
            if a[i] < min1:
                if a[i] < min2:
                    min2 = min1
                    min1 = a[i]
            elif a[i] > min1:
                if a[i] < min2:
                    min2 = a[i]
        eq = (((min2 & min1) ^ (min2 | min1)) & (min2 ^ min1))
        return eq,min1,min2
    for i in range(1,len(a)):
        res = findminandmax(a,i)
        if len(stack) == 0:
            stack.append(res)
        elif len(stack)!=0:
            var = stack.pop()
            if res > var:
                stack.append(res)
            else:
                stack.append(var)
    return stack[0]
print(andXorOr(a))
