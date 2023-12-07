def givenstr(s):
    s1 = list(s)
    length = len(s1)
    final = 0
    if s1[length - 1 ] == "1,2,3,4,5,6,7,8,9,0":
         final = length
    else:
         final = length - 1
    return final



print(givenstr("abcdefghijklmnop1"))



