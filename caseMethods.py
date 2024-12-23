# name="BraInZimA"
# print(name.upper())
#
# print(name.lower())
#
# print(name.capitalize())


# Project : take a text from user and ask user to do what and do that according to user
txt=input("Enter your text:")
todo=input("Enter what you want (Upper, lower, capitalize):")
if todo == 'upper':
    print("Converted Text: ", txt.upper())
elif todo == 'lower':
    print("Converted Text: ", txt.lower())
elif todo == 'capitalize':
    print("Converted Text: ", txt.capitalize())
else:
    print("invalid Choice!")