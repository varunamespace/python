a = [1,2,3,4,5,6]
l = []
def two_sum(a,tar,ftar):
    dict = {}
    for i in a:
        rem = tar - i
        if i not in dict:
            dict[rem] = i
        else:
            if dict[i]+rem+tar == ftar:
                l.append((dict[i],rem,tar))

def three_sum(a,ftar):
    for i in range(len(a)):
        two_sum(a,a[i],ftar)
    return l
print(three_sum(a,6))
