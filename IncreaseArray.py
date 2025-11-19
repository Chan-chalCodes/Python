arr = list(map(int, input().split()))
inc = int(input("Enter increament value:"))
newArr = []
for i in arr:
    val = i+inc
    newArr.append(val)
print(newArr)