n = int(input())
arr = list(map(int, input().split()))
total_sum = 0
for i in range(n):
    total = (i+1)*(n-i)
    contri = total*arr[i]
    total_sum += contri
print(total_sum)