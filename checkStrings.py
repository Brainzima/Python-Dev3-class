# a = "Brainzima"
# print(len(a))
# lenth = len(a)
#
# print(a)
# print(lenth)

# Question: take a name of user from the user and display it but the name should be less than 10 characters
# name = input("Enter your name:")
# lenth = len(name)
# if lenth > 10:
#     print("Sorry Na cholbe, name should be under the 10 characters")
# else:
#     print("Great,",name)

# Question: take a mobile of user from the user and display it but the mobile should be less than 10 or more than 10 characters
# mobile = input("Enter your mobile no:")
# lenth = len(mobile)
# if lenth == 10:
#     print("You have a great number",mobile)
# elif lenth > 10:
#     print("Bahut jadha hua nahi chalega")
# elif lenth < 10:
#     print("Bahut kam h")
# else:
#     print("Nhi pta")


#membership operation check
# txt = "Brainzima Innovation is completely offers the innovative courses to make the students more innovators"
# print("courses" in txt)

#Question: take a input about the user and find if the user is done bca or b.tech then display cutom message
# about = input("Tell me more about you? :-")
# if "bca" in about:
#     print("You are doing welll with BCA keep it up and join brainzima")
# elif "btech" in about:
#     print("You are doing welll with BTech keep it up and join brainzima")
# elif "done" not in about:
#     print("First of all you have to complete the course")
# else:
#     print("best of luck for the future, brainzima can make your future bright so join brainzima")


#thora advance
about = input("Tell me more about you? :-")
if "bca" in about and "done" in about:
    print("You are doing welll with BCA keep it up and join brainzima")
elif "btech" in about and "done" in about:
    print("You are doing welll with BTech keep it up and join brainzima")
else:
    print("Done your course first, brainzima can make your future bright so join brainzima")