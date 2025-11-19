A = int(input("Enter range for Odd numbers:"))
for i in range(1, A+1):
    if i % 2 != 0:
        print(i, end=' ')