arr = list(map(int, input().split()))
target = int(input("enter target:"))
count = 0
for ele in arr:
    if target == ele:
        count += 1
print(count)