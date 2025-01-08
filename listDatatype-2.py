# insert method
# course = ['DCA','ADCA','CFA']
#
# print(course)
#
# course.insert(2, 'DTP')
#
# print(course)

# Extend list
bcourse = ['DCA','ADCA','CFA','DTP','ADCS']
pcourse = ['C', 'C++','C#', 'Java', 'PHP', 'Python']

print('Basic Courses :-', bcourse)
print('Programming Courses:-', pcourse)

# traditioanl but two different lists
print('All Courses :-', bcourse,pcourse)

# to create a all courses list
courses = []
courses.extend(bcourse)
courses.extend(pcourse)
print('All Courses :-',courses)
