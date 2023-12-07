def linear_sum(S,n):
    if n == 0:
        return 0
    else:
        return linear_sum(S,n-1) + S[n-1]

s=[1,2,3,5,6,7,8]
print(linear_sum(s,3))

