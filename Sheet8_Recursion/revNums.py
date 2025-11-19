def reverse(n):
    if n == 1:
        print(1)
    else:
        print(n)
        reverse(n-1)
n = int(input())
reverse(n)