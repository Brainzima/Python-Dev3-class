# Take input of five subjects math, science, ssc, hnd, eng and display division
# marks >=300 1st
# marks >=225 2nd
# marks >=150 3rd
# marks <150  Fail
print("************************************")
math=int(input("Enter marks of Math:"))
sc=int(input("Enter marks of Sc:"))
ssc=int(input("Enter marks of SSc:"))
hnd=int(input("Enter marks of Hnd:"))
eng=int(input("Enter marks of Eng:"))
print("************************************")
total = math + sc + ssc + hnd + eng
print("Your Obtained Marks is :",total)
if total >= 300:
    print("You have achieved a 1st Division trophy")
elif total >= 225:
    print("You have achieved a 2nd Division trophy")
elif total >= 150:
    print("You have achieved a 3rd Division trophy")
else:
    print("You have achieved a Zero Division trophy which is Fail but not failure")
