####total no of ways for coin change

"""dp = [0]*(a+1)
for i in range(1,len(dp)):
    if i-1>=0 and i-2>=0 and i-3>=0:
        dp[i] = max(dp[i - 1]+1, dp[i - 2]+1, dp[i - 3]+1)
    if i-1>=0 and i-2>=0:
        dp[i] = max(dp[i - 1]+1, dp[i - 2]+1)
    if i-1>=0:
        dp[i] = max(dp[i - 1]+1, dp[i])
print(dp[-1])
"""
a = 4
c = [1,2,3]
def tot(a,c):
    if a == 0:
        return 1
    elif a<0:
        return 0
    res = 0
    for i in c:
        res = res + tot(a-i,c)
    return res
print(tot(a,c))

