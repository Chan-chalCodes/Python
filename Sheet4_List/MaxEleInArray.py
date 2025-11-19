arr = list(map(int, input().split()))
a = -float("inf")
b = float("inf")
for i in arr:
    if(a < i):
        a = i
    if(b > i):
        b = i
print("Max element: ",a)
print("Min element: ", b)
