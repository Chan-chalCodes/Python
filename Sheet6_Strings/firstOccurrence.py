Str = input()
target = int(input())
count = 0
for s in Str:
    if(chr(target)==s):
        count+=1
if count>0:
    print(count)
else:
    print("not exist!")