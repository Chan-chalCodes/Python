n = int(input())
for i in range(n):
    S = input()
    rev = ''
    n = len(S)
    for j in range(n):
        if(S[j] == S[n-j-1]):
            rev += S[j]
    if(S == rev):
        print(1)
    else:
        print(0)