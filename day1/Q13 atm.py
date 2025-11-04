a=int(input("enter the account number : "))
b=int(input("enter a pin : "))
c=int(input("total amount enter"))
print(''' 1=check balance 
      2=deposite
      3=withdraw''')
i=int(input())
if(i==1):
    pin=int(input("enter a pin"))
    if(b==pin):
        print("balance=",c)
elif(i==2):
    pin=(int(input("enter pin")))
    if(b==pin):
        dep=int(input("enter depositr amount : "))
        c=dep+c
        print("total balance=",c)
elif(i==3):
    pin=int(input("enter pin "))
    if(b==pin):
        withd=int(input("enter eithder amount "))
        c=withd-c
        print("total amount",c)
else:
    print("invalid ")