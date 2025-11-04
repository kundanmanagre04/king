# a=0
# b=1
# c=0
# n=int(input())
# for i in range(n):
#     print(a,end=' ')
#     c=a+b
#     a=b
n=int(input())
a=0
b=1
c=0
for i in range(n):
    for j in range(i):
        print(a,end=' ')
        c=a+b
        a=b
        b=c
    print()