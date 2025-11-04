# def append(data,mylist):
#     print(mylist+data)

# values=[1,2,3]
# a=[5]
# append(a,values)

# data=[1,2,3]
# a=[90]
# print(data+a)

#****** functions ******
# def function_name():
#     print('hi')
#     print('hello')
#     print('bye')
# function_name()
# for i in range(5):
#     print(i)
# function_name()

#Q waf to print table of 2

# def table(n):     #// n is parameters defination ke time pe parameters hota hai
#     for i in range(1,11):    
#         print(f"{n} x {i} = {n*i}")
# a=int(input())
# table(a)  #a is argument calling time pe argument hota hai

# function 4 type ke hote hai based in parameter and return type 
# 1)parameter with return type
# 2) parameter without no return type
# 3) no parameter with return type
# 4) no parameter without return type

# def fun():
#     print('hi')
#     return 0
# # print(fun())
# a=fun()
# print(a)

# def my(n):
#     print('hii')
#     return n
# print(my(5))
# no of parameter and no of argument barabar hona chayiye

# Q) waf to count repeated element 
# def mycount(data,n):
#     count=0
#     for i in data:
#             if i==n:
#                 count+=1
#     print(count)

# data=[5,10,5,3,5,3,5,32,56,4,5,6,1,3,2,4]
# mycount(data,5)

# def remove(data,n):
#     s=[]
#     count=0
#     for i in data:
#         if i!=n or count==1:
#             s=s+[i]
            
#         else:
#             count=1   
#     print(s)
# data=[1,2,3,4,5,5,3,5,3,5,6,1]
# remove(data,5)

# def sum(s,t):
#     sum=0
#     for i in range(s,t+1):
#         sum+=i
#     print(sum)
# sum(2,5)

# def sqr(collection):
#     for i in collection:
#         s=i**2
#         print(s)
# collection=[1,2,3,4,5]
# sqr(collection)


# a=[2,3,4,5,6,7]
# target=7
# for i in a:
#     for j in a:
#         if i+j==target:
#             print(i,j)

# a=[2,3,4,5,6,7]
# target=7
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==target:
#             print(i,j)

# def add(a,b=0):
#     print(a+b)
# add(10)

# def add(a=[]):
#     a.append(1)
#     print(a)
# add()       //[1]
# add()       //[1,1]

# def foo(k,v,n={}):
#     n[k]=v
#     print(n)
# foo('a',90)
# foo('b',100)

# def f1(a):
#     return a
# def add():
#     val=f1(3)
#     val1=5
#     return val+val1
# print(add())


#****bubble sort****
# a=[6,5,4,3,2,1,7,8]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             temp=a[i]
#             a[i]=a[j]
#             a[j]=temp
# print(a)
        
#merge sort
# a=[6,5,4,3,2,1]
# start=0
# end=len(a)
# if start<"mid"
# data='123'
# for i in range(2,1,-1):
#     print(data[i],end=' ')

#bubble sort
# data=[6,5,4,3,22,30,18,21,2]
# length=len(data)
# for i in range(length):
#     for j in range(length-1):
#         if data[j]>data[j+1]:
#             data[j],data[j+1]=data[j+1],data[j]
# print(data)