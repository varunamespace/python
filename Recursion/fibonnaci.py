def own_fibo(n):
    if n<=1:
        return n
    else:
        return n + own_fibo(n-1)

def good_fibo(n):
    if n<=1:
        return (n,0)
    else:
        (a,b) = good_fibo(n-1)
        return (a+b,a)


print(own_fibo(5))
print(good_fibo(5))