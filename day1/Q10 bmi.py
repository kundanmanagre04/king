a=int(input("enter a weight : "))
b= int(input("enter a height :"))
bmi=a/b**2
if(bmi<18.5):
    print("underweight")
elif(18.5<=bmi or bmi<24.9):
    print("normal weight")
elif(25<=bmi or bmi<29.9):
    print("overweight")
elif(bmi>=30):
    print("obesity")