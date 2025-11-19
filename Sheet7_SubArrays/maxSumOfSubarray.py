n = int(input())
arr = list(map(int, input().split()))
maxi = -float("inf")
sum = 0
for ele in arr:
    sum += ele
    if sum > maxi:
        maxi = sum
    if sum < 0:
        sum = 0
print(maxi)
