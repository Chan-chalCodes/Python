n = int(input())
temp = list(map(int, input().split()))
sum = 0
count = 0
for i in temp:
    sum += i
avg = sum/n

for i in temp:
    if(i > avg):
        count += 1
print(count)