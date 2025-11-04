age=int(input("enter your age"))
if(age<=1):
    print("infant")
elif(age<=4 and age>=2):
    print("toddler")
elif(age<=12 and age>=5):
    print("child")
elif(age<=19 and age>=13):
    print("teenager")
elif(age<=59 and age>=20):
    print("adult")
else:
    print("60 year old" )