# def f1():
#     return "hello"
# def f2():
#     a=5
#     return f1(),a,"aaa"
# print(f2())
# a=90
# def borawan():
#     global a
#     a=10

#     print(a)
# borawan()
# print(a)

# ****** roman to integer ******
# a='IV'
# b={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
# sum=0
# prev=0
# for i in reversed(a):
#     value=b[i]
#     if value<prev:
#         sum-=value
#     else: 
#         sum+=value
#         prev=value
# print(sum)

# ****** lamda function ******

# add=lambda a,b:a*b
# a=add(10,5)
# print(a)
# print(add(10,20))

# mal=lambda a,b:a*b
# add=lambda a,b:a+b
# sub=lambda a,b:b-a
# divi=lambda a,b:b//a
# print(mal(10,20))
# print(add(10,20))
# print(sub(10,20))
# print(divi(10,20))

# data=[[1,2],[3,4]]
# data2=[j for x in data for j in x]
# print(data2)

# data=[(lambda x:x**2)(i) for i in range(1,6)]
# print(data)


