def num(n):
    if n == 1:
        print(n)
    else:
        num(n-1)
        print(n)
n = int(input())
num(n)