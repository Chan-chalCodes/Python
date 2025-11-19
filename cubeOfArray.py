arr = list(map(int, input().split()))
newArr = []
for ele in arr:
    cube = ele**3
    newArr.append(cube)
print(newArr)