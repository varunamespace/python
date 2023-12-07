import re
def Check(string, vowels):
    str_list = re.findall(f'[{vowels}]', string, re.I)
    print(len(str_list))
    return str_list
vowels = "aeiouy"
string = str(input())
print(Check(string, vowels))
