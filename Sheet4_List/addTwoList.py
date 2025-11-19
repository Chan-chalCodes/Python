list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
result = []
for i in range(len(list1)):
    result.append(list1[i]+list2[i])
print(result)