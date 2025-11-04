a=int(input("enter the year to check if it is a leap year or not : "))
if(a%4==0 and a%100!=0):
    print(f"{a} this is a leap year ")
elif(a%400==0):
    print(f"{a} this is a leap year ")
else :
    print(f"{a} this is not a leap yerar")
