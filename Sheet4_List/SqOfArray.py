arr = list(map(int, input().split()))
newArr = []
for ele in arr:
    sq = ele*ele
    newArr.append(sq)
print(newArr)