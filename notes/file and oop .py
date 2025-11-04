'''file handling'''
'''append'''
# f=open("demo.txt",'a')
# f.write("helllo jit ")
# f.close()

'''with open se append'''
# with open("demo.txt",'a') as f:
#     f.write("aayush")

'''write'''
# f=open("demo.txt",'w')
# f.write('kundan')
# f.close()

'''write with open'''
# with open("demo.txt",'w') as f:
#     f.write("kundan")

'''read'''
# f=open("demo.txt",'r')
# a=f.read()
# print(a)

'''read eith open'''
# with open("demo.txt","r") as f:
#     a=f.read()
#     print(a)

'''seek and tell'''
# f=open("demo.txt")
# f.seek(7)   # seek 7 number par pointer ko mover kar dega or tail current position dikhayega pointer ki
# a=f.read(6)  #7 se 6 character read karega read ke andar jitni value hogi utne charcter read karega
# print(a)
# f.close()

'''leetcode 27'''
# a=[0,1,2,2,3,0,4,2]
# b=[]
# c=[]
# count=0
# value=int(input("enter a value : "))
# for i in a:
#     if i==value:
#         count+=1
#         i='_'
#         c.append(i)
#     else:
#         b.append(i)
# k=len(a)-count
# print(k)
# b=b+c
# print(b)
'''leetcode 28'''
# s='leetcode'
# f=input(f"enter find substring in {s} : ")
# a=f[0]
# if f in s : 
#     print(s.index(a))
# else:
#     print(-1)

'''oop is way of solving real word problem'''
'''oop features=1)data security 2)no of line is less 3) scalability 4) data hiding '''
'''pilllors=class,object,inheritance,encapsulation,data abstraction,polymorphism,'''
# class car:
#     color='red'
#     model=2025
#     def start(self):
#         print('car started ')
#     def start_traveling(self):
#         print("going for ujjain mahakal tempal")
# bmw=car()
# car.color='red'
# # bmw.start()
# # bmw.start_traveling()
# bmw.color="black"
# print(bmw.color)

# audi=car()
# print(audi.color)

'''3 attribute and 2 method'''
# class bike:
#     color="black"
#     model=2025
#     avrage=60
#     def start(self):
#         print("bike is started ")

#     def stop(self):
#         print("bike is stop at destination ")
# splendor=bike()
# bike.color="zblack"
# print(splendor.color)
# print(splendor.model)
# print(splendor.avrage)
# splendor.start()

'''class variable(static variable) => 1) inside the class and outside of method is called class variable '''
'''2)class variable object to object same rahegi sabhi object ke liye same rahegi '''
'''way if defind class variable => 1)inside the class and outside of method 2)inside the method 3)class method decorator 4) static method decorator'''
