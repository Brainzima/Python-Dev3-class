# name="brainzima"
# print(name)
#
# print(name[3:7])
#
# print(name[3:])
#
# print(name[:7])




# Project: Take text from the user and display the range and ask for the range user wants to display then display that range of characters
txt=input("Enter whatever you want:")
print("Entered: ",txt)
lenth =len(txt)
print("Enter the range from 0 to",lenth)
start = int(input("Start from:"))
end = int(input("End to:"))

if start > lenth:
    print("Invalid Range!")
else:
    print(txt[start:end])



