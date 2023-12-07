def revchar(s,n):
    if n == 1:
        return s[0]
    else:
        return s[n-1] + revchar(s,n-1)
        #return revchar(s,n-1) + s[n-1]

c = 'hello'
print(revchar(c,len(c)))