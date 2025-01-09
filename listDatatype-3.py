# course = ['DCA','ADCA','CFA','DTP','ADCS', 'DTP']
#
# print(course)
#
# # remove item from list using value
# course.remove('DTP')
# print(course)
#
# # remove item from list using index
# course.pop(3)
# print(course)


# Project: Take a consent to delete items from list
course = ['DCA','ADCA','CFA','DTP','ADCS', 'Python']
print(course)
action = input("How do you want delete? (Value or Index) :")
if action == 'value':
    value = input("Enter Value: ")
    course.remove(value)
    print(course)
elif action =='index':
    index = int(input("Enter Index: "))
    # index = index-1
    index -= 1
    course.pop(index)
    print(course)
else:
    print('Galat hai ye.')