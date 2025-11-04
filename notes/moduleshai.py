''' from notes import * ==> all variable function are import '''
# import notes10
# print(notes10.spp)
# from notes10 import output,spp
# spp=1
# print(spp)
# output(90,190)/

'''buit in modules '''
'''math module'''
# import math
# # print(math.pi)  # 3.14
# # print(math.ceil(23.1))  #23.1 ko nearest int me badle ga 24 aage ke
# # print(math.floor(90.9)) #90.9 ko nearest int me badle ga 90 piche ke
# print(math.factorial(5)) # 5 ka factorail nikal ke print karega 120
# print(math.sqrt(3)) # sqare rooot of 3 
# print(math.cbrt(3)) #cube rooot of 3
# print(math.gcd(16,10)) # 
# print(math.pow(2,3)) # 2 ki power 3 ka result dega

# def gcd(a,b):
#     chota_nu=min(a,b)
#     bada_nu=max(a,b)
#     new=[]
#     for i in range(1,chota_nu+1):
#         if bada_nu%i==0 and chota_nu%i==0:
#             new.append(i)
#     return max(new)
# print(gcd(90,13))

'''sys system module'''
# import sys
# sys.stdout.writelines("hello world")  # display hello world without using print()
# a=sys.stdin.readline()
# sys.stdout.writelines(a)

'''data and time module'''
# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.now().date())
# print(datetime.datetime.now().time())
# print(datetime.datetime.now().hour)
# print(datetime.datetime.now().minute)
# print(datetime.datetime.now().second)
# print(datetime.date(2070,12,12))
# print(datetime.datetime.weekday(datetime.date(2025,9,28)))
# print(datetime.datetime.toordinal(datetime.datetime.now()))
# days={0:'monday',1:'tuesday',2:'wednesday',3:'thusday',4:'friday',5:'saturday',6:'SUNDAY'}
# print(days[datetime.datetime.weekday(datetime.datetime.now())])

'''oprating system os module '''
import os 
# print(os.listdir("/"))    ##print karega directry ko
# os.chdir("file path")    #directry ka path cahnge karega
# print(os.listdir())   #print karega directry ko
# print("output is => ",os.curdir)    #current working directory ka path print kar dega
# print(os.getcwd())   #curent working directry ko print karega 
# os.mkdir("myfile")             #file bana dega ya folder mtfile name se

'''system module'''
import sys
# print(sys.version)        # current ka version or kab installed kiya gaya bata dega
# a=sys.stdin.readline()   # input lega using sys moodule  , stdin is system input lega
# print(a)
# sys.stdout.writelines("hello world")  # stdin is system output this is a ouput dega 
