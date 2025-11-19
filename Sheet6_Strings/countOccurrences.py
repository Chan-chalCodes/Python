# Str = "abobc"
# count = Str.count("bob")
# print(count)
str = "abobob"
word = "bob"
count = 0
for i in range(len(str)-len(word)+1):
    # res = ""
    # for j in range(len(word)):
    #     res += str[i+j]
    # if res == word:
    #     count += 1
    if str[i]=='b' and str[i+1]=='o' and str[i+2]=='b':
        count+=1
print(count)