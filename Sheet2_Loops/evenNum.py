A = int(input("Enter range for even numbers:"))
for i in range(2, A+1):
    if i % 2 == 0:
        print(i, end=' ')