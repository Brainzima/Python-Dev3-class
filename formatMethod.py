# without variable name
# txt = "Course name is {} Fees of this course is {} only."
# print(txt.format("Python",6500))
# print(txt.format(6500, "Python"))

# with variable name
# txt = "Course name is {name} Fees of this course is {fee} only."
# print(txt.format(fee=6500, name="Python"))


# Project: Ask to user of his name, mobile and item , rate, qnty and display calculate this
name=input("Enter your name:")
mobile=input("Enter your mobile:")
item=input("Enter your item:")
rate= int(input("Enter your rate:"))
qnty=int(input("Enter your qnty:"))
amount = rate * qnty
txt = "Hey {name}, ({mobile}). You have purchased {item} of {qnty} quantities with the rate of {rate}. Now your total bill is {amount}"
print("******************************************************************************")
print(txt.format(name=name,mobile=mobile,item=item,rate=rate,qnty=qnty,amount=amount))