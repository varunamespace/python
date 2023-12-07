def s(a):
    if a == 0:
        return 0
    return int(a%10)+s(int(a/10))
print(s(12))
print(1//10)
print(int(1/10))
