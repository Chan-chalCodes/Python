percent = float(input("Enter your percentage:"))
if(percent >= 85 and percent <= 100):
    print("Grade: A+")
elif(percent >= 65 and percent < 85):
    print("Grade: A")
elif(percent >= 45 and percent < 65):
    print("Grade: B")
elif(percent >= 25 and percent < 45):
    print("Grade: C")
elif(percent < 25):
    print("Grade: D")
else:
    print("Invalid percentage.")


