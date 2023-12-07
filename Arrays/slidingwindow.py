a = str(99)
def check(a):
    dict = {}
    for i in a:
        if i in dict:
            return False
        dict[i] = 1
    return True

def top(a):
    res = check(a)
    val = 0
    val1 = 0
    if res:
        val = int(a)+1
        while check(val):
            return val
            val = val + 1
    val1 = int(a)+1
    while check(val1):
        return val1


top(a)




print(check(a))





