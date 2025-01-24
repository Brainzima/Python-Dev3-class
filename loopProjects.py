# Project 1
# take number from the user and display its square upto10 times
# num = int(input("Enter number:"))
# i = 1
# while i <= num:
#     print(i*i)
#     i += 1



# Project 2
#  take number of inputs from user then user will enter the value of those inputs and finally display its sum
# inputs = int(input("How many number you want to add? - "))
# i = 1
# sum = 0
# while i <= inputs:
#     num = int(input("Enter the value of num:"))
#     sum = sum+num
#     i+=1
# print("Sum of all numbers: ",sum)

# Project 3:
# make the triangle pattern using asterisk
# num = int(input("How many stars you want to print? - "))
# for a in range(1,num+1):
#     for b in range(a):
#         print('*', end="")
#     print()

# 1

# num = int(input("How many stars you want to print? - "))
# for a in range(1,num+1):
#     for b in range(a):
#         print(a, end=" ")
#     print()


# 2

num = int(input("How many stars you want to print? - "))
for a in range(1,num+1):
    for b in range(a):
        print(b, end=" ")
    print()