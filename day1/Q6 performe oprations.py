a=int(input("enter first no : "))
op=input("enter oprator : ")
b=int(input("enter second no : "))

if(op=='+'):
    print(a+b)
elif(op=='-'):
    print(a-b)
elif(op=='*'):
    print(a*b)
elif(op=='/'):
    print(a/b)
else:
    print("wrong oprator")