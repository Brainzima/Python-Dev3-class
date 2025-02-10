# import datetime
# tareek = datetime.datetime.now()
# print(tareek)
# print(tareek.year)
# print(tareek.month)
# print(tareek.day)
#
# print(tareek.strftime('%A'))
# print(tareek.strftime('%a'))
# print(tareek.strftime('%d'))
#
# pastkadate = datetime.datetime(2045,5,10)
# print(pastkadate)
# print(pastkadate.strftime('%A'))


# Project demo
import datetime
stu_name = 'Demo Kumar'
stu_ad = datetime.datetime(2025,1,10)
ajkadate = datetime.datetime.now()

stu_d = stu_ad.strftime('%d')
# print(stu_d)
ajka_d = ajkadate.strftime('%d')
# print(ajka_d)
print(ajkadate.strftime('%j'))

if(stu_d == ajka_d):
    print(stu_name,'Your Bill is generated!')
else:
    print('Enjoy...')