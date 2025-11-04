'''upward multi inheritance'''
# class c1:
#     def __init__(self):
#         print("c1 constructor")
#     def by(self):
#         print(" i am from c1")
# class c2(c1):
#     def __init__(self):
#         print("c2 constructor")
#     def by(self):
#         print(" i am c2 method")
# class c3(c1):
#     def __init__(self):
#         print("c3 constructor")
#     def by(self):
#         print(" i am c3 method")
#         a=c1()
        
# obj=c3()
# obj.by()
'''downword inheritance'''
# class c1:
#     def m1(self):
#         print("i am from c1")
# class c2:
#     def m1(self):
#         print("i am from c2")
# class c3(c1,c2):
#     def m1(self):
#         print("i am from c3")
#         super().m1()
# obj=c3()
# obj.m1()


'''method overloading => ek method se different different work karwana based on arguments(method do multiple opration based on arguments)'''
# class c1:
#     def m1(self,a=0,b=0,c=0):
#         if b==0 and c==0 and a>1:
#             print("one args",a)
#         elif a!=0 and b!=0 and c!=0:
#             print("three args",a+b+c)
#         elif c==0 and b!=0:
#             print("two args",a*b)
#         else:
#             print("no args")
# o=c1()
# o.m1()

'''method overridding '''
# class c1:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def  __add__(self,other):
#         n1=self.a+other.a
#         n2=self.b+other.b
#         return n1,n2


# obj1=c1(12,34)
# obj2=c1(17,16)
# print(obj1.__add__(obj2))

# class c1:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def  __mul__(self,other):
#         n1=self.a*other.a
#         n2=self.b*other.b
#         return n1,n2


# obj1=c1(10,10)
# obj2=c1(15,16)
# print(obj1.__mul__(obj2))

class c1:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def  __div__(self,other):
        n1=self.a*other.a
        n2=self.b*other.b
        return n1,n2


obj1=c1(10,10)
obj2=c1(15,16)
print(obj1.__div__(obj2))