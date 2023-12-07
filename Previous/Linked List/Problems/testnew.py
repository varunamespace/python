"""ar = [1,2,3,4,5,6]
tar = 8
def fun(a,tar):
    dict = {}
    for i in a:
        res = tar-i
        if res in dict:
            return (res,dict[res])
        dict[i] = res
print(fun(ar,tar))
"""
#roman numerals i/p:"ix"...o/p:"9" i/p:"x" o/p:10
a = "xi"
dict = {"i":"+1-","v":"+5-","x":"+10-"}


