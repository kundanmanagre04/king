# mutable area list,set,dictionary "data change karne par locaation same rahe gi "
# in mutable is int,float,str,complex, "data change hone par id change hogi"
#data same + mutable = id same
#data same + immutable  = id different
  


        # **bitwise oprator**
# uses in binary no,
# bin function use to binary number chech bin(12)=ob1100
# print(bin(4) ans=ob101111 true=1 false=0
#types= or=!,and=&,not=~,xor=^ (same bit become zero different is 1),shift(<<left----->>right)zzzzzzzzzz
# print(bin(35))


# #         **** LOOPS  ****
# #types of loop= for loop,while loop
# for i in range(1,5):
#     print(i)

#range functions use to start and stop at point range(start,end)
# for i in range(1,5):
#     print(i)
#print(1,1) ans=empty
#print(range(10,1)) ans=empty
# print(range(1,5,1)) ans=1,2,3,4 "forward said me 1 dafault hota hai"
# print(range(10,1,-1)) ans=10,9,8,7,6,5,4,3,2 "reverse karega"
#print(range(1,10,2)) ans=1,3,5,7,9 "2nd data element ko skip karega but 2 numbers ko skip karta jayega"
#range(10,1) is not work because forword me work nhi karega
#
# data=[5,10,15,16]
# for i in data:
# #     print(i)
# # end=' ' end is used to print in single line
# data=[1,2,3,4,5,6]
# for i in data:
#     print(i**2,end=' ')
# data='welcome to jit'
# for i in data:
#     print(i,end='')
#     if i==" ":
#         print("")  space is str " " is consider as space

# a=(1,2,3,4,5)  tuple
# for i in a:
#     print(i**2)
# a={'a':1,'b':2,'c':3}

# print(a['a'])  dictonary access using a[i]
# for i in a:
#     print(i,'--',a[i])

# for i in range(1,10):
#     print(i,end=" ")


# a=int(input("enter the number : "))
# for i in range(1,11):
#     print(i*a,end=" ")

#even or odd
# a=int(input("starting range : "))
# b=int(input("enter ending of range : "))
# for i in range(a,b+1):
#      if(i%2==0):
#           print("even")
#      else:
#           print("odd")

#prime number
# a=int(input('enter a number : '))
# b=0
# for i in range(2,a):
#     if(a%i==0):
#         b=1
# if(b==0):
#     print("this is a prime number : ")
# else:
#     print("this is not a prime number : ")
# a=5
# b=a
# for i in range(a):
#     for j in range(b):
#         print("*")
# print("")
# b-=1
