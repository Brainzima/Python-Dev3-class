# Project 1:
stars = "******************************"
print(stars)
name = input("Enter Name: ")
item = input("Enter Item: ")
rate = int(input("Enter Rate: "))
qnty = int(input("Enter Quantity: "))
gst = int(input("Enter GST Rate: "))
state = input("Enter State: ")
print(stars)
amount = rate * qnty
total = 0
print("Name :",name)
print("Item :",item)
print("Rate :",rate)
print("Quantity :",qnty)
print("GST Rate :",gst)
print("State :",state)
print("Amount :",amount)
print(stars)
if state == 'Bihar':
    sgst = (amount * gst / 100) / 2
    cgst = sgst
    print("SGST :",sgst)
    print("CGST :",cgst)
    total = amount + sgst + cgst
else:
    igst = amount * gst / 100
    print("IGST :", igst)
    total = amount + igst

print("Total Amount :",total)
