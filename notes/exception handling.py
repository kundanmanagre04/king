'''exception error (error handling)'''
'''try block me error aaya to excepyt block execute hoga or agar try block me error nhi aaya to else block execute hoga '''
'''finaly block ke under jo likha hai wo execute hoga hi error aaye ya nhi aaye '''
# try:
#     a=int(input())
#     b=int(input())
#     print(a/b)
# except ZeroDivisionError:
#     print("do not use zero in b ")
# except Exception as e:
#     print(e)
# else:
#     print("no error will occure ")
# finally:
#     print("it will executed always")
# while True:
#     try:
#         a=int(input("enter a first number : "))
#         b=int(input("enter a second number : "))
#         print(a/b)
#         break
#     except Exception as e:
#         print(e)

# def rac(n):
#     for i in range(n+1):
#         for j in range(n+1):
#             if i==0 or j==0 or i==n or j==n or i==j or i+j==n:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()
# try:
#     rac(6) 
# except Exception as e:
#     print(e)
#     '''changest longest non repeating character in str'''

# '''reverse string'''
# s="hello"
# a=''
# for i in s:
#     a=i+a
# print(a)

'''uppercase half'''
# s='kundan'
# a=''
# half=len(s)//2
# for i in range(half):
#     a=a+s[i].capitalize()
# for i in range(half,len(s)):
#     a=a+s[i]
# print(a)

'''small capital '''
# s='KUNdAN'
# if s!=s.upper():
#     print("not all capital ")
# else:
#     print("all capital")

'''sub string program'''
# s='kundan'
# n='kun'
# if n in s:
#     print("yes")
# else:
#     print("no")

'''remove substring'''
# s='kundan'
# a=input(f"enter remove sub string in this string {s} ")
# b=''
# for i in range(s.index(a[0])):
#     b+=s[i]
# for i in range(s.index(a[-1])+1,len(s)):
#     b+=s[i]
# print(b)


# s='kundan'
# a=input()
# if a in s:
#     print(s.replace(a,""))
# else:
#     print(f"this substring not in {s}")

'''palindrom string '''
# s=input("enter a str : ")
# a=s[-1:-(len(s))-1:-1]
# if s==a:
#     print(f"this is a palindrom string {s}")
# else:
#     print(f"this is not a palindrom string {s}")

# def check_palindrom(s):
#     s1=''
#     for i in s:
#         s1=i+s1      <= # reverse  the string 
#     if s1==s:
#         print('yes')
#     else:
#         print("no")
# check_palindrom("aa")
'''non repeating longest string'''
# data='abcfghbpqrstbcd'
# new=data.split(" ")
# print(new)
# red=0
# for i in new:
#     if len(i)>red:
#         red=len(i)
#     else:
#         pass
# print(red)

# new=[]
# data='abcfghbpqrstbcd'
# a=''
# a=a+data[0]
# for i in range(1,len(data)):
#     if ord(data[i-1])==ord(data[i])-1:
#         a+=data[i]
#     else:
#         new.append(a)
#         a=data[i]
# new.append(a)
# print(new)
'''sum of digit'''
# data=456
# n1=data//100  #1
# n2=(data-n1*100)//10   #2
# n3=(data-(n1*100+n2*10)) #3
# print(n1+n2+n3)
'''sum of all digit using recursen'''
# def sum_num(n):
#     if n==0:
#         return 0
#     else:
#         last=n%10
#         return last+sum_num(n//10)
# print(sum_num(456))