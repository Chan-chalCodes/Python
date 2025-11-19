list1 = list(map(int, input().split()))
n = len(list1)
for i in range(0, n//2):
    list1[i], list1[n-1-i] = list1[n-1-i], list1[i]
print(list1)