n = int(input())
count = 0
for i in range(n):
    lst = input().split()
    marks = int(lst[0])
    attent = int(lst[1])
    if(marks >= 75 and attent >= 80 ):
        count += 1
print(count)

    
