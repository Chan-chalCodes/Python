n = int(input())
price = list(map(int, input().split()))
count = 0
for i in range(1, n):

    if price[i] > price[i-1]:
        count += 1
print(count)
