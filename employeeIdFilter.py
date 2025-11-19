n = int(input())
emp_id = list(map(int, input().split()))
count = 0
for id in emp_id:
    if(id % 2 == 0):
        print(id, end=" ")
        count += 1
if count == 0:
    print(-1)
