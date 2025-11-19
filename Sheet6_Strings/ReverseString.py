Str = input()
s = Str.split()
for word in s:
    length = len(word)
    rev = ''
    for i in range(length-1, -1, -1):
        rev += word[i]
    print(rev, end=" ")