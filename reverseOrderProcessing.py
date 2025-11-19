n = int(input())
ids = list(map(int, input().split()))
res = []
count = 0
for id in ids:
    if id % 5 == 0:
        res.append(id)
    else:
        count += 1
if(count == n):
    print(-1)
res.reverse()
for ans in res:
    print(ans, end=" ")