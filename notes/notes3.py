# # # # # # # #           LOOP         
# # # # # # # #    ********** PATTERN PRINTING ********
# # # # # # # for i in range(0,4):
# # # # # # #     for j in range(0,i+1):
# # # # # # #         print("*",end=' ')
# # # # # # #     print("")

# # # # # # =ans=
# # # # # # * 
# # # # # # * * 
# # # # # # * * * 
# # # # # # * * * * 

# # # # # # for i in range(4,0,-1):
# # # # # #     for j in range(i-0):
# # # # # #         print("*",end=' ')
# # # # # #     print(" ")

# # # # # # * * * *  
# # # # # # * * *  
# # # # # # * *  
# # # # # # *  
# # # # # for i in range(4):
# # # # #     for j in range(4-i):
# # # # #         print("*",end='  ')
# # # # #     print('')

# # # # for i in range(5):
# # # #     for j in range(i+1):
# # # #         if i==j or i==4 or j==0:
# # # #             print("*",end=" ")
# # # #         else:
# # # #             print(" ",end=' ')
# # # #     print()
# # # # * 
# # # # * * 
# # # # *   * 
# # # # *     * 
# # # # * * * * * 

# # # for i in range(4):
# # #     for j in range(4):
# # #         if i==0 or j==0 or i==3 or j==3:
# # #             print("*",end=' ')
# # #         else:
# # #             print(" ",end=' ')
# # #     print()

# # # * * * * 
# # # *     * 
# # # *     * 
# # # * * * * 

# # # rows=int(input("enter roe"))
# # # col=int(input("enter colume"))
# # # for i in range(rows+1):
# # #     for j in range(col-1):
# # #         if i==0 or j==0 or i==rows-1 or j==col-1:
# # #             print("*",end=' ')
# # #         else:
# # #             print(' ',end=' ')
# # #     print()

# # a=int(input("enter "))
# # for i in range(a):
# #     for j in range(i+1):
# #         if i==j or i==a-1 or j==0:
# # #             print("*",end=" ")
# # #         else:
# # #             print(" ",end=' ')
# # #     print()

# # # a=int(input("enter no "))
# # # if a%2==0:
# # #     a=a+1
# # # for i in range(a):
# # #     for j in range(a):
# # #         if i==j or i==a-j-1 or i==0 or i==a-1 or j==a-1 or j==0:
# # #             print("*",end=" ")
# # #         else:
# # #             print(" ",end=' ')
# # #     print()

# # a=int(input("enter no "))
# # if a%2==0:
# #     a=a+1
# # for i in range(a):
# #     for j in range(a):
# #         if  i==a-j-1 or  i==a-1 or j==a-1 :
# #             print("*",end=" ")
# #         else:
# #             print(" ",end=' ')
# #     print()



# a=int(input("enter"))
# for i in range(a):
#     for j in range(a):
#         if j+i==2 or j-i==-2 or i==j-2 or j+i==-2 or i+j==(a//2)*3:
#             print("x",end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# n=9
# for i in range(n):
#     for j in range(n):
#         if i+j==n//2 or j-i==n//2 or i-j==n//2 or i+j==(n//2)*3 :
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()

# for i in range(5):
#     for j in range(5-i):
#         print(" ",end=' ')
#     for k in range(i):
#         print('*',end=' ')
#     for m in range(i):
#         print("*",end=' ')
#     print()

# for i in range(5):
#     for j in range(i+1):
#         print(' ',end=' ')
#     for k in range(5-i):
#         print("*",end=' ')
#     for m in range(4-i):
#         print("*",end=' ')
#     print()

# for i in range(5):
#     for j in range(i):
#         print("x",end=' ')
#     print()
# for i in range(3,0,-1):
#     for j in range(i):
#         print("x",end=' ')
#     print()


# n=7
# for i in range(n):
#     for j in range(n):
#         if i+j==n//2 or j-i==n//2  or i==n-4:
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()