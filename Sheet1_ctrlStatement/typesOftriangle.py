angle1 = int(input("Enter first angle:"))
angle2 = int(input("Enter second angle:"))
angle3 = int(input("Enter third angle:"))
if(angle1 == 90 or angle2 == 90 or angle3 == 90):
    print("Right Angle")
elif(angle1 > 90 or angle2 > 90 or angle3 > 90):
    print("Obtuse Angle")
else:
    print("Acute angle")