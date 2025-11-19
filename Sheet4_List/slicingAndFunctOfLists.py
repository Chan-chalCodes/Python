list = [2,4,6,8,10,12,14,16,18,20]
print(list[:])
print(list[::])
print(list[2:5])
print(list[2:])
print(list[2::])
print(list[:2])
print(list[::2])
print(list[1::2])
print(list[2:10:2])

list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
print(len(list))
print(list[-2 :-5: -1])
print(list[-2:])
print(list[-2::])
print(list[:-2])
print(list[::-2])
print(list[::-1])

mylist = [1.4, 2, 3, 4, 5, 'Suyash']
mylist.reverse()
print(mylist)

s = "Hello everyone how are you"
print(s.split())
s = "Hello-everyone-how are you"
print(s.split("-"))
word = 'Suyash:Chaudhary:Noida'
print(word.split(':'))
t = "23456"
print(t.split())
t = "2 3 4 5"
print(t.split())

l1 = [1, 2, 3, 5, 8, 9]
l2 = [3, 4, 5 , 6, 7, 10]
result = l1 + l2
print(result)
result1 = l1 * 3
print(result1)
