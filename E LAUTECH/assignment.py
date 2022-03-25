side1 = int(input("Enter first side"))
side2 = int(input("Enter second side"))
side3 = int(input("Enter third side"))
if side1==side2==side3:
    print("it is a equilateral triangle")
elif side1==side2 or side1==side3 or side2==side3:
    print("it is a isoselece triangle")
elif side1==90 or side2==90 or side3==90:
    print("it is a right angle triangle")
else:
    print("it is a scalene triangle")            