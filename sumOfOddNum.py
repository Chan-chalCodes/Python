A = int(input("Enter range for Odd numbers:"))
sum = 0
print("Sum of all Odd numbers b/w 1 to",A,":")
for i in range(1, A+1):
    if i % 2 != 0:
        sum += i
print(sum)