a=int(input("enter first side of triangle : "))
b=int(input("enter second side of triangle : "))
c=int(input("enter third side of triangle : "))

if(a+b>c or b+c>a or a+c>b):
    print("this is a triangle")
else:
    print("this is not a triangle")