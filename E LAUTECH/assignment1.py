num = float(input("Enter a rating"))
num1 = 0.0
num2 = 0.4
num3 = 0.6
if num == num1:
    print("Unacceptable performance")
    print(num1*2400)
elif num == num2:
    print("Acceptable performance")
    print(num2*2400)
elif  num >= num3:
    print("Meritious performance")
    print(num3*2400)
else:
    print("invalid rating")           