# Q1: Print the first and last value from list
# names = ['Rakesh','Mukesh','Rajesh','Nitesh','Jitesh','Lokesh','Kumesh']
#
# print(names[0],names[-1])

# Q2: Ask the user to enter 5 numbers. Calculate and print the average of those numbers.
# method-1
# num1 = int(input('Enter Number1:'))
# num2 = int(input('Enter Number2:'))
# num3 = int(input('Enter Number3:'))
# num4 = int(input('Enter Number4:'))
# num5 = int(input('Enter Number5:'))
# sum = num1+num2+num3+num4+num5
# average = sum/5
# print(average)

# method-2
sum = 0
for a in range(5):
    num = int(input('Enter Number:'))
    sum += num
print(sum/5)
