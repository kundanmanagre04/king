# ****data type****
# data='Welcome To Jit'
# print(data.replace("jit",'iit'))
# print(data.join("iit"))
# print(data.ljust(8,'jit'))
# print(data.rjust(15,"*"))
# print(data.strip(' '))
# print(data.swapcase())

#dublicat lo hataye
# data='welcome to to my my collage jit jit'
# s=''
# for i in data.split():
#     if i not in s:
#         s+=i
#         s+=' '
# print(s)
# for i in data.split():
#     count=0
#     for j in data.split():
#         if i==j:
#             count+=1
#             break
#     if count==1:
#         s+=i
#         s+=''
# print(s)


# data='welcome to to my my jit jit '
# s=''
# for i in data.split():
#     a=data.count(i)
#     if a>1 and i not in s:
#         print(f"{i} is count is {a}")
#         s+=i

    
# s=input()
# new=s.split()
# print(len(new[-1]))

#leet code 
# data=list(input())
# output=[]
# unique=set(data)
# for i in unique:
#     count=0
#     for j in data:
#         if i==j:
#             count+=1
#     output.append(i)
#     if count>1 and count<10:
#         output.append(count)
#     elif count>0 and count>9:
#         new_count=str(count)
#         for i in new_count:
#             output.append(i)
# print(len(output))


# data=[1,2,3,4,5,6]
# data[3:5]=[0,0,0,0,0,0]
# print(da

# 8 0 0
# 5 0 3 
# 5 3 0
# 2 3 3
# 2 5 1
# 7 0 1
# 7 1 0 
# 4 1 3  

# 8 5 3
# 8 0 0
# 5 0 3
# 5 3 0
# 2 3 3
# 0 5 3 
# 3 2 3 
# 6 2 0

