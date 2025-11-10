# '''we can modify attributes'''
# '''obj to obj same rahe value(data) to called class(static) variable and obj to obj change ho value to instance variable'''
# '''class variable declaration variables => 1) inside class ouside method 2)inside method using classname.variablename=value 3) using classmethod decorator @nameofdecorator  4) using staticmethod decorator '''

# # class car:
# #     model=2025
# #     @classmethod  #this is use to declare class variable its classmethod decorator
# #     def m2(cls):
# #         cls.data=12345
# #         print(cls.model)
# #     @staticmethod  #its not assosiated with class or method 
# #     def m3():
# #         data2=90
# #         print(data2)
# # skoda=car()
# # skoda.m3()

# # skoda.m2()
# # print((skoda.data))


# '''instance variable =>obj to obj value chenge hogi '''
# '''declaration of instance variable => '''

# # class c2:
# #     def m1(self,a,b): #self is not key word replace with any name 
# #         self.instance1=a # this is instance variables
# #         self.instance2=b
# #     def display(self):
# #         print(self.instance1,self.instance2)
# # obj=c2()
# # obj.m1(10,20)
# # obj.instance1=500 # using object change the value 
# # print(obj.instance1) # using object print a
# # obj.display()
# # newobj=c2()
# # newobj.m1(2,5)
# # newobj.display()

# '''what is self => self is also a instance of class like object 2) witout self we can not call method 3) without self not declare instance variable 4) we can not access 5) we can not modify 6) we can not use instance variable in other method '''

# '''constructor => it is a method '''
# '''when you create a object of class constructor automatically execute '''
# # class c1:
# #     def __init__(self,a,b):    # this is constructor 
# #         self.a=a
# #         self.b=b
# #         print(self.a+self.b)
# .0
# # obj=c1(4,6)

# '''constructor method not return '''
# # class c3:
# #     def __init__(self,a):
# #         self.a=a
# #     def m2(self):
# #         self.a+=1                       

# # obj=c3(5)
# # obj.m2()
# # obj.m2()
# # obj.m2()
# # print(obj.a)

# # class c3:
# #     def __init__(self,a):
# #         print("hi")
# #     def __init__(self):
# #         print('hii')
# # obj=c3()
# # obj=c3(1)

# '''destructor => its destroy data'''
# # class c3:
# #     data=90
# #     def m1(self,a):
# #         self.a=a
# #         print("i an m1")
# # obj1=c3()
# # del obj1.data  # it delete the data
# # print(obj1.data)

# # class c4:
# #     data=90
# #     def m1(self):
# #         del c4.data
# # obj=c4()
# # obj.m1()
# # print(obj.data)


# '''decorator => it is way to change the behaviour of existiong function or method without writting code in to it we use decorator with @ symbal followerd by decorator name '''

# # def mydecorator(function_name):# function_name=display()
# #     def wrapper():
# #         print("i am wrapper executed before function  ")

# #         function_name()  # display() calling

# #         print("i am wrapper executed after function ")
# #     return wrapper() # its return wraper ccalling

# # @mydecorator  # display() as argument in decorator and its called 
# # def display():
# #     print("hello world ")

# # def multiply(fun):
# #     def wrapper():
# #         c=fun(10,5)
# #         print(c*10)
# #     return wrapper()
# # @multiply
# # def add(a,b):
# #     c=a-b
# #     return c

# # def multi(fun):
# #     def wrapper(*args):
# #         a=fun(*args)
# #         print(a*10)
# #     return wrapper
# # @multi
# # def dis(a,b):
# #     return b-a
# # dis(5,10)

# '''create decorator to count recursion call factorial'''
# # count=0
# # def my(function):
# #     def abc(n):
# #         global count
# #         count+=1
# #         a=function(n)
# #         return a
# #     return abc
# # @my
# # def fec(n):
# #     if n==0:
# #         return 1
# #     return n*fec(n-1)
# # print(fec(5))
# # print(count)
 
# '''create decorator to count recursion call factorial 2nd approach'''
# # def count(func):
# #     global count
# #     count=0
# #     def wrapper(n):
# #         global count
# #         count+=1
# #         return func(n)
# #     return wrapper
# # @count
# # def fact(n):
# #     if n==0:
# #         return 1
# #     return n*fact(n-1)
# # print(fact(5))
# # print(count)


# class ims:
#     def __init__(self):
#         self.product_name=[]
#         self.quantity=[]
#         self.price=[]
#         self.qua_pri=[]
#     def add(self,p_name,p_quantity,p_price):
#         self.product_name.append(p_name)
#         self.quantity.append(p_quantity)
#         self.price.append(p_price)
#         self.qua=dict(zip(["quantity","price"],[p_quantity,p_price]))
#         self.qua_pri.append(self.qua)
#         self.data=dict(zip(self.product_name,self.qua_pri))
#     def display_record(self):
#         print(self.data)  
    
# obj=ims()
# while True:
#     product=input("enter a product name : ")
#     quantity=int(input("enter the quantity : "))    
#     price=int(input("enter a price of product : "))
#     obj.add(product,quantity,price)
#     choice=input("press Y to enter more items\n press N to exit ")
#     if choice=='N' or choice=='n':
#         break

# # obj.display_record()  
#  def s(*a);
#       b=0
#       for i in a;
#       b+=i
#    return b
# print(s(3,2,3,4,2