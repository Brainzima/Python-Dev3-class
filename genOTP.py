import random

# numbers = [1,2,3,4,5,6,7,8,9,0]
#
# print(random.choice(numbers))

# otp generator
# numbers = ['1','2','3','4','5','6','7','8','9','0']
# otp = ''
# for a in range(6):
#     otp += random.choice(numbers)
#
# print(f"Your OTP: {otp}")


# password generator
randomList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '[', ']', '{', '}', '|', ';', ':', ',', '.', '/', '?']
password = ''
for a in range(8):
    password += random.choice(randomList)

print(f"Your Password: {password}")