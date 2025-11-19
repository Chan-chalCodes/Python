arr = list(map(int, input().split()))
target = int(input("Enter your target:"))
for i in range(len(arr)):
    if arr[i] == target:
        print("target present at index = ",i)
# l1 = [1,2,3,4,4,5]
# l2 = [5,6,7,8]
# result = []
# for i in range(len(l2)):
#     result.append(l1[i] + l2[i])
# print(result)



