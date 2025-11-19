Str = input()
newStr = Str + Str
result = ""
for S in newStr:
    if S == S.lower():
        if S in 'aeiou':
            result += "#"
        else:
            result += S
print(result)
