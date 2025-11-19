arr = list(map(int, input().split()))
print("Odd elements: ")
for ele in arr:
    if(ele % 2 != 0):
        print(ele, end=" ")
print()
print("Even elements: ")
for ele in arr:
    if(ele % 2 == 0):
        print(ele, end=" ")