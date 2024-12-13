# Take input of five subjects math, science, ssc, hnd, eng and display division
# marks >=300 1st
# marks >=225 2nd
# marks >=150 3rd
# marks <150  Fail
#student should have to achieve atleast of more than 29 marks to pass
# if any one subject is less than 30 then student will be failed

print("************************************")
math=int(input("Enter marks of Math:"))
sc=int(input("Enter marks of Sc:"))
ssc=int(input("Enter marks of SSc:"))
hnd=int(input("Enter marks of Hnd:"))
eng=int(input("Enter marks of Eng:"))
print("************************************")
total = math + sc + ssc + hnd + eng
print("Your Obtained Marks is :",total)

# method 1

# if (math > 29 and sc > 29 and ssc > 29 and hnd > 29 and eng > 29):
#     if total >= 300:
#         print("You have achieved a 1st Division trophy")
#     elif total >= 225:
#         print("You have achieved a 2nd Division trophy")
#     elif total >= 150:
#         print("You have achieved a 3rd Division trophy")
#     else:
#         print("You have achieved a Zero Division trophy which is Fail but not failure")
# else:
#     print("You are Fail")



# method 2

if (math < 30 or sc < 30 or ssc < 30 or hnd < 30 or eng < 30):
    print("You are Fail")
else:
    if total >= 300:
        print("You have achieved a 1st Division trophy")
    elif total >= 225:
        print("You have achieved a 2nd Division trophy")
    elif total >= 150:
        print("You have achieved a 3rd Division trophy")
    else:
        print("You have achieved a Zero Division trophy which is Fail but not failure")