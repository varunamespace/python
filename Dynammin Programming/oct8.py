#a = [1,2,3,1]
a = [6,7,1,3,8,2,4]
def rob(a):
    st = 0
    sk = 0
    for i in range(0,len(a),2):
        st = a[i]+st
    for j in range(1,len(a),2):
        sk = a[j]+sk
    return max(st,sk)

def rob1(a,ind):
    if ind>=len(a):
        return 0
    steal = a[ind]+rob1(a,ind+2)
    skip = rob1(a,ind+1)
    return max(steal,skip)

def rob2(a):
    l = [0]*(len(a)+2)
    for i in range(0,len(a)):
        l[i+2] = max(a[i]+l[i],l[i+1])
    return l[-1]

print(rob2(a))