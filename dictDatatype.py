# info = {
#     'name':'Rajik',
#     'age':525,
#     'mobile': 7979797997,
#     'email':'rajik@gmail.com',
#     'course':'Python'
# }

# print(info)
#
# print(type(info))

# access any single data
# print(info['email'])


# Project: User can access the information if userid and password is correct
info = {
    'userid':'1001',
    'password':'pass@123',
    'name':'Rajik',
    'age':525,
    'mobile': 7979797997,
    'email':'rajik@gmail.com',
    'course':'Python'
}

print("********************************")
print("Access your detail")
print("********************************")
userid = input("User Id: ")
password = input("Password: ")
print("********************************")
if userid == info['userid'] and password == info['password']:
    txt = "Hey, {name}, Welcome to Dashboard. Your course {course} is Amazing.";
    print(txt.format(name=info['name'], course=info['course']))
else:
    print("Userid or Password is Incorrect.")