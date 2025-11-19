Str = input()
subStr = input()
if subStr in Str:
    pos = Str.find(subStr)
    print(pos)
else:
    print("Substring not exist!")