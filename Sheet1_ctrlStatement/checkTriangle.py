angle1 = int(input("Enter first angle:"))
angle2 = int(input("Enter second angle:"))
angle3 = int(input("Enter third angle:"))
sum = angle1+angle2+angle3
if(sum == 180):
    print("yes, Triangle is valid.")
else:
        print("No, Triangle is not valid.")