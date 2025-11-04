# data=[1,2,3,3,4,4,5]
# a=[x**2 for x in data ]
# print(a)


# ******* dictonary comprehension ******
# ==> it is a concept in which we genratae data element in keys and value pair

# data={chr(k):k for k in range(65,91)} # this is all alphabet a to z in dictionary
# print(data)

# data={'a':23,True:3444,121:'adfsfdf',3.14:"pie"}  # list se dictinary ki value ko access karna
#  print(data[3.14])

# data['a']={'age':20,'name':"rohan"} # agar data me a key hai to update ho jayegi or nhi hogi to new key ban jayegi
# print(data)

''' it is a colllectiom of keys and values pair
it is a mutable
it is orderd  before 3.7 version of python its unordered
'''

# def f1(a=[]):
#     a.append(1)  #
#     return a
# print(f1())
# print(f1())

# def f1(a,b=set()):    # its mutable only tuple not mutable
#     b.add(a)
#     return b
# print(f1(1))
# print(f1(2))
# print(f1(3))

""" highly ordered function """

# def add(a,b):
#     return a+b

# def opration(a,b,c):
#     return c(a,b) # add(10,20) return value 30 here
# print(opration(10,20,add))

# def compose(a,b,c):
#     return a(b(c))   # output is 5
# add=lambda x:x+1
# mul=lambda x:x*x
# print(compose(add,mul,2))

# def cal(a,b,c,d,e):
#     print(b(e))
#     print(c(e))
#     print(d(e))
#     return a(e)
# add=lambda x:x+x
# sub=lambda x:x-1
# mul=lambda x:x*x
# div=lambda x:x/x
# print(cal(add,sub,mul,div,5))

''' Variable Argument Function  (* abc ) * is compalsary its is a varArgu'''

# def sum(*argument):
#     sum=0
#     for i in argument:
#         sum+=i
#     print(sum)
# sum(10,10,10,10,6)


# def sum(a):
#     sum=0
#     for i in a:
#         if int(i)%3==0 or int(i)%5==0:
#             sum+=int(i)
#     print(sum)

# a=input().split(" ")
# sum(a)

# def d1(a,b,*c):
#     new=a+b
#     n2=sum(c)      #  4,15
#     print(new,n2)
# d1(1,3,1,2,3,4,5)

# def flat_list(data):
#     empty=[]
#     for i in data:
#         for j in i:
#             empty.append([j])
#     return empty                    #[[1], [2], [3], [4], [5], [6], [7], [8], [9]]
# data=[[1,2,3],[4,5,6],[7,8,9]]   
# print(flat_list(data))  

# def reverse(s):
#     for i in range(-1,-(len(s))-1,-1):    # this function reverse the string
#         print(s[i],end='')
# s='aayush'
# reverse(s)

# def reverse(s):
#     a=' '
#     for i in s:
#         a=i+a          # this is reverse a string and forword loop
#     return a
# data='jit collage'
# print(reverse(data))

''' Recursion ==> a function called it self multiple type its called it recursive function '''

#def f1(n):
#     if n>=11:
#         return 0
#     else:
#         print(n)
#     return f1(n+1)
# f1(1)
# def f1(n):
#     if n<0:
#         return 0
#     else:
#         print(n)
#     return f1(n-1)
# f1(10)

# def f1(n,sum):
#     if n>10:
#         return sum
#     else:
#         sum+=n
#         return f1(n+1,sum)
# print(f1(1,0))

# facti=1
# def fact(n,factorial):
#     if n<=1:
#         return factorial
#     else:
#         factorial=factorial*n
#     return fact(n-1,factorial)
# print(fact(3,facti))

# s=''
# def reverse(a,b,s):
#     if len(b)==a:
#         return s
#     else:
#         s=b[a]+s
#         return reverse(a+1,b,s)
# print(reverse(0,"hello",s))

# data=[12,23,45,23,34]
# def display(a):
#     element=len(data)
#     if a==element:
#         return 0
#     else:
#         print(data[a],end=" ")
#         return display(a+1)
# print(display(0))

# data=[12,23,45,23,34]
# a=len(data)-1
# def display(a,data):
#         if a<0:               # reverse the list
#                 return 1
#         else:
#                 print(data[a],end=" ")
#                 return display(a-1,data)
# display(a,data)

