n = int(input())
codes = list(map(int, input().split()))
arr = []
for i in range(n):
    repeat = 0
    for j in range(n):
        if codes[i] == codes[j] and i != j:
            repeat = 1
            break
    if repeat == 0:
        arr.append(codes[i])

for ele in arr:
    print(ele, end=" ")

if len(arr) == 0:
    print(-1)

