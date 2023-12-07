def power(x,n):
    if n == 0:
        return 1
    else:
        return x * power(x,n-1)
print(power(2,13))

for i in range(1,6):
    print(13//i, end=" ")


