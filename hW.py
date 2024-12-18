# 1
# Even or Odd Checker:
# Take a number as input.
# Determine whether the number is even or odd.
# num % 2 == 0

# 1 Solution:
# num=int(input("Enter a number to check the number is odd or even:"))
# if(num % 2 == 0):
#     print(num,"is a even number")
# else:
#     print(num,"is a odd number")


# 2
# Leap Year Checker:
# Take a year as input.
# Determine whether the year is a leap year.
# year % 4 == 0

# 2 solution:
# year=int(input("Enter a year to check the year is leap or not :"))
# if(year % 4 == 0):
#     print(year,"is leap year.")
# else:
#     print(year,"is not a leap year.")

# 3
# Traffic Light Simulator:
# Take a color as input (red, orange, green).
# Print the appropriate action based on the color:
# Red: "Stop"
# orange: "Slow down"
# Green: "Go"

# 3 solution:
# indicator = input("Enter a color of traffic light (red, orange, green) :")
# if indicator == 'red':
#     print("Ruko, Sabar kro.")
# elif indicator == 'orange':
#     print("hawle hawle!")
# elif indicator == 'green':
#     print("Chalaja Dost!")
# else:
#     print("Oops! Enter valid light indicator")

# 4
# item=userInput
# rate=userInput
# qnty=userinput
# amount=?
# discount=?
# discount condition
# amount>5000   - 1000
# amount>3000   - 500
# amount>2000   - 300
# amount>1000   - 100
# amount<1000   - 0
#
# net payable amount=?

# 4 solution:
print("************************************************")
item = input("Enter item name:")
rate = float(input("Enter the rate:"))
qnty = int(input("Enter the Quantity:"))
amount = rate * qnty
if amount > 5000:
    discount = 1000
elif amount > 3000:
    discount = 500
elif amount > 2000:
    discount = 300
elif amount > 1000:
    discount = 100
else:
    discount = 0
print("************************************************")
print("Item:",item)
print("Quantity:",qnty)
print("Rate:",rate)
print("Gross Total:",amount)
print("You Saved:",discount)
print("Net Payable Amount:",amount-discount)
print("************************************************")
