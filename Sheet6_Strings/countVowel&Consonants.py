n = int(input())
for i in range(n):
    Vowel = 0
    Consonant = 0
    S = input()
    n = len(S)
    for j in range(n):
        s = S[j]
        # if(s=='A' or s=='a' or s=='E' or s=='e' or s=='I' or s=='i' or s=='O' or s=='o' or s=='U' or s=='u'):
        if s.upper() in 'AEIOU':
            Vowel += 1
        else:
            Consonant += 1
    print(Vowel, end=" ")
    print(Consonant)