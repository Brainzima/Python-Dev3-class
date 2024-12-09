num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
num3=int(input("Enter number3:"))

# if num1>num2 and num1>num3:
#     print("Number 1 is bigger.")
# elif num2>num1 and num2>num3:
#     print("Number 2 is bigger")
# else:
#     print("Number 3 is bigger")

if num1==num2==num3:
    print("Barabar")
elif num1>num2 and num1>num3:
    print("Number 1 is bigger.")
elif num2>num1 and num2>num3:
    print("Number 2 is bigger")
else:
    print("Number 3 is bigger")