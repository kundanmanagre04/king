# data='c++'
# print(data[2:])    # //stop default me len(data) tak jayega or start 0 se default lega

# def f1():
#     return lambda x,y:x*y
# a=f1()                // a ke andar f1() ka return aayega 
# print(a(10,20))

# t=int(input())
# for i in range(t):
#     a,b=map(int,input().split())
#     if a>=b:
#         print("0")
#     else:
#         if (b-a)//8==(b-a)/8:
#             print((b-a)//8)
#         else:
#             print(((b-a)//8)+1)

# import math
# t=int(input())
# for i in range(t):
#     a,b=map(int,input().split())
#     if a>=b:
#         print("0")
#     else:
#            print(math.ceil((b-a)/8)

# a=[1,2,3,4,5,6]
# data=["*"*i+str(i)+"*"*i for i in a]
# print(data)
# data=[f"{"*"*i}{i}{"*"*i}" for i in a]      ['*1*', '**2**', '***3***', '****4****', '*****5*****', '******6******']
# print(data)
# data=[x for x in range(1,11) if x%2==0 ]
# print(data)

# data=[(lambda x:x**2)(x) for x in range(1,11) if x%2==0]
# print(data)

# a=['abc','pqr','stu']
# data=[x[::-1] for x in reversed(a)]              //reversed string using slicing
# print(data)
# for i in reversed(a):
#     print(i[::-1],end=" ")

# data=[1,2,3]
# new=[]
# new.append([])
# for i in range(len(data)):
#     new.append([data[i]])             # //sublist print karna hai
#     for j in range(len(data)):
#         if i<j:
#             new.append([data[i],data[j]])
# print(new)

# data='jiwefhbibfendnfouidfwjd'
# count={}
# unique=set(data)
# for i in unique:
#     c=0
#     for j in data:
#        if i==j:
#         c+=1
#     count[i]=c
# print(count)

# import tkinter as tk
# windows=tk.Tk()
# windows.geometry("700x700")
# windows.config(bg='yellow')
# label=tk.Label(windows,text="WELCOME ",font=('bold,25'),background='red',)
# label.pack()
# windows.mainloop
# data=[1,2,5,7,8]
# for i in data:
#     l1=[]
#     if i==i:
#         l1.append([i,i+1])
#         l1.append([i+4])
#         l1.append([i+6,i+7])
#     print([l1])
#     break



# data=[1,6,3,2,5,17,8]
# for i in range(len(data)):
#         for j in range(len(data)-i-1):
#             if data[j]>data[j+1]:
#                 data[j],data[j+1]=data[j+1],data[j]
# print(data)

# data=[6,79,80,90]
# for i in range(len(data)):
#     if data[i]>data[i+1] and data[i+2]:
#         print(data[i])
#     elif data[i+1]<data[i] and data[i+2]:
#         print(data[i+2])
#     else:
#         print(data[i+1])
    
       
#         break
# data=[1,2,3,4,8,9,10]
# new=[]
# result=[]
# for i in range(len(data)):
#     if data[i-1]+1==data[i]:
#         new.append(data[i])
#     else:
#         result.append(new)
#         new=(data[i])
# result.append(new)
# result.pop(0)
# print(result)

# data="abcefgijl"
# data=[]
# for i in data:
#   data.append(ord(i)) 
    
# data=["apple,banana"]
# data.count(data)
# print(data)

# data=[1,2,3,1,3,6,8,9,8,7]
# sum=0
# new=[]

# for i in range(len(list)):
#     if data[i]==data[i+1]:
#         i+=1
#         if data[i]!=data[i+1]:
#             new.append(data[i])

# print(data)

