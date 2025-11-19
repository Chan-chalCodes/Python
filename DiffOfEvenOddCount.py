arr = list(map(int, input().split()))
countEven = 0
countOdd = 0
for ele in arr:
    if ele % 2 == 0:
        countEven += 1
    else:
        countOdd += 1
print(countEven-countOdd)