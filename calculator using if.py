#menus
print("calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

#input choice
ch=int(input("Enter choice(1-4):  "))
#addition
if ch==1:
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    c = a+b
    print("Sum = ",c)
#subraction
elif ch==2:
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    c = a - b
    print("Difference = ",c)
#multiplication
elif ch==3:
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    c = a*b
    print("Product = ",c)
#division
elif ch==4:
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    c = a/b
    print("Quotient = ",c)
else:
    print("Invlaid Choice")