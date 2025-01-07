# [] - square bracket/ bari bracket
# () - paranthesis / small bracket
# {} - curly braces / manjhli bracket

# list variable
# list_example = [1, "Brainzima Computer", 12542.55, "Katihar"]

# show values
# print(list_example)
# print(type(list_example))
# print(list_example[0])
# print(list_example[1])
# print(list_example[2])
# print(list_example[3])

# print("Institute Name:", list_example[1])
# print("Institute Address:", list_example[3])

# change list item
# list_example[3] = "Maldah"
# print(list_example)
# print("Institute Address:", list_example[3])

# Insert using append method
# print(list_example)
# list_example.append("7979864304")
# print(list_example)


# Project: take inputs of name, mobile, email, course and display a info card as one varibale
info = []
name = input("Enter Name:")
info.append(name)
mobile = input("Enter Mobile:")
info.append(mobile)
email = input("Enter Email:")
info.append(email)
course = input("Enter Course:")
info.append(course)

print(info)

action = input("Would you like change your course? (yes/no) - ")
if action == 'yes':
    info[3] = input("Enter new Course:")
    print("Updated Info is: ", info)
elif action == 'no':
    print("OK, As you wish........")
else:
    print("Oops, Invalid Action.")
