a=int(input("enter a amount od prodact : "))

if(a>1000):
   print("final price ",a-a*0.1)
elif(a>500 and a<1000):
   print("final price is ",a-a*0.05)
else:
   print("sorry no discount final price is",a)