n = int(input())
lst = list(map(int, input().split()))
count = 0
longest = 0
for i in lst:
    if i == 0:
        count += 1
        if count > longest:
            longest = count
            count = 0
print(longest)