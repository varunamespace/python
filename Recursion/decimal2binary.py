l = []
a = ''
def d2b(a):
    if a == 0:
        return
    l.append(int(a%2))
    a = a + str(a%2)
    d2b(int(a//2))

def db(a):
    if a==0:
        return 1
    else:
        return (a%2)+10*db(int(a//2))
print(db(13))

