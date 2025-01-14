num1 = 45456
num2 = 600
# print( num1 > num2 )

# result = num1 > num2

# print(result)

# if result == True:
#     print("Num1 is big")
# elif result == False:
#     print("Num2 is big")

# name = bool('')
# print(name)

# name = bool('Brainzima')
# print(name)

# name = bool(416545)
# print(name)

# Project
name = input("Your Name: ")
# print("Hi,",name)
# method 1
# if name == '':
#     print("Please enter valid name!")
# else:
#     print("Hi,",name)

# method 2
if bool(name):
    print("Hi,", name)
else:
    print("Please enter valid name!")