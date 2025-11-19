n = int(input())
lst = list(map(int, input().split()))
target = int(input())
count = 0
for i in range(n):
    for j in range(i+1, n):
        res = lst[i]+lst[j]
        if(res == target):
            count += 1
print(count)
