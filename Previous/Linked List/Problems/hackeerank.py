def largestRectangle(a):
    res, count, rev, norev = 0, 0, 0, 0
    l = []
    for i in range(len(a)):
        if a[i] < a[(len(a) - 1) - i]:
            norev = norev + 1
        else:
            rev = rev + 1
    if rev > norev:
        a = a[::-1]
    mini = a[0]
    for i in range(len(a)):
        val = a.pop(0)
        count = count + 1
        if mini >= val:
            mini = val
        res = mini * count
        l.append(res)
    return (max(l))
