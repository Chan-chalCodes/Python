A = int(input("Enter range for even numbers:"))
sum = 0
print("Sum of all even numbers b/w 1 to",A,":")
for i in range(2, A+1):
    if i % 2 == 0:
        sum += i
print(sum)