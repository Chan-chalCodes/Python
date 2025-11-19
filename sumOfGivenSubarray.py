n = int(input())
arr = list(map(int, input().split()))
index = list(map(int, input().split()))
sum = 0
for i in range(index[0]-1, index[1]):
    sum += arr[i]
print(sum)