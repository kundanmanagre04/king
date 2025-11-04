# a=int(input("enter days of week : "))
# if(a==1):
#     print("monday")
# elif(a==2):
#     print("tuesday")
# elif(a==3):
#     print("wednesday")
# elif(a==4):
#     print("thusday")
# elif(a==5):
#     print("friday")
# elif(a==6):
#     print("saturday")
# elif(a==7):
#     print("sunday")
# else:
#     print("wromng ")


a={1:'monday',2:'tuesday',3:'wednesday',4:'thursday',5:'friday',6:'saturday',7:'sunday'}
b=int(input("enter a number "))
if(b in a):
    print(a[b])
    
