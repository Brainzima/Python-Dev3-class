# isAplhaNumerics
# txt = "Bera"
# txt = input("Enter Anything:")
# print(txt.isalnum())

# is Alpha
# txt = "234"
# txt = input("Enter Anything:")
# print(txt.isalpha())

# Project : Take input from the user and display if the entered value is alphabet and numerics or not
# txt = input("Enter Anything:")
# check = txt.isalnum()
#
# if check == True:
#     print("Your entered inputs are mix of Alphabets and Numbers.")
# else:
#     print("You have entered some special characters sayad")

# Project : Take input from the user and display if the entered value is what?
txt = input("Enter Anything:")
alnum = txt.isalnum()
num = txt.isdigit()
alpha = txt.isalpha()

if alpha==True:
    print("Your entered Values are Aphabets.")
elif num==True:
    print("Your entered Values are Numbers.")
elif alnum==True:
    print("Your entered Values are mix of Aphabets and NUmbers.")
else:
    print("Your entered Values are Special Characters.")
