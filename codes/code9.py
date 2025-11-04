#*********** DATA TYPES***********
#*********** STRING **************
# data='hello' // this is a string stored in data using single quote 
# data='''welcome to jit session
#         end of this line'''   #// document string is genrated throw triple qu0te ''' -''' or "" -""
# print(data[0])
# data="indore@gmail.com"
# new=data.upper()                                      //uper case me transform
# print(new)
# new=data.lower()
# print(new)                                         //lower case me
# new=data.endswith('@gmail.com')
# print(new)                                       //@gmail.com last me hona chaye 

# data="12k"
# re=data.isnumeric()
# print(re)                                       //string me nhumeric hai ya nhi
# re=data.isalnum()
# print(re)                                      //alpha numeric dono ho

# data="title format"
# # re=data.title()                           //TITLE FORMAT BANAYEGA
# # print(re)
# re=data.translate('123')
# print(re)

# data='abc123xyz45'
# for i in range(-1,-len(data)-1,-1):
#      if data[i].isnumeric():                     //string se number alag kara
#             print(data[i],end=' ')

# print(ord('a'))                                           // ord function character ko ascii value me convert karta hai
# print(chr(97))                                           //chr fubnction int ko ascii se charater me badalta hai

# n=6
# a=65
# for i in range(5):
#         for j in range(i):
#                 print(chr(a),end=' ')
#                 a+=1
#         print()

# a,b,c=map(int,input("enter a number ").split(' '))
# if a>b and a>c:
#     if b>c:
#         print(b)
#     else:
#         print(c)
# elif b>a and b>c:
#     if a>c:
#         print(a)
#     else:
#         print(c)
# else:
#     if a>b:
#         print(a)
#     else:
#           if a>b:
#                     print(a)

# Q strong number 
# a=145
# b=a
# sum=0
# while a>0:
#     last=a%10
#     a//=10
#     fact=1
#     for i in range(1,last+1):
#         fact=fact*i
#     sum+=fact
# print(sum)
# if sum==b:
#     print("this is strong number")
# else:
#     print("this is not a strong number")


# *************** print circle*******************
# n=int(input("enter a number : "))
# r=n//2
# for i in range(n):
#     for j in range(n):
#         distance= ((i-r)**2+(j-r)**2)**0.5
#         if (abs(distance-r)<0.5):
#             print("*",end='')
#         else:
#             print("",end=' ')
#     print()
# a=[2,7,11,14]
# target=9
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i]+a[j]==target:
#             print(i,j)
#data =123
#new =0
#while data>0:
 #   last = data % 10
 #   new =new*10+last
 #   data//=10
#print(new)

#n = 123
#new=0
#sum=0

#while n>0:
#    old = n % 10


 #   sum = sum + old
#    n//=10

#print(sum)



#n=2334
#check=n
#sum=0

#while n>0 :
 #   last = n % 10
  #  fact=1
  #  for i in range(1,last+1):
 #       fact*=i
  #  sum+=fact
 #   n//10
#if sum==check:
#    print("yes Strong no")
#else:
#    print("NOT STRONG NO")


# n = 153
# count = 0
# b=n
# while (n>0):
#     n//=10
#     count = count+1
#     arm=1

# while(b>0):
#     last = n%10
#     e =last**count
#     sum+=e
#     b//=10

# if sum==num:
#     print("yes its a armstrong")
# else:
#     print("no")

'''no of character in string '''
# s="hello"
# count=0
# for i in range(len(s)):
#     if s[i]==" ":
#         pass
#     else:
#         count+=1
#print(count)
