''' random number genrate karega random.randit(star,end) range given between '''
#import random 
# num=random.randint(1,10)
# print(num)
'''random name choose karega'''
# names=['kundan','aayush','maz','deepak']
# print(random.choice(names))
'''0 to 1 print random number float values'''
# print(random.random())
'''random number range ke bitch'''
#print(random.randrange(1,5,3))
'''email par otp send karna '''
# import smtplib,random,ssl
# app_pass='raqy jzox sjsz wbrd'
# email="aayushpatidar0924@gmail.com"
# to='kundanmanagre04@gmail.com'
# otp=random.randint(1111,9999)
# body=f"your otp for login is {otp} "
# with smtplib.SMTP("smtp.gmail.com",465,context=ssl.create_default_context()) as s:
#      s.login(email,app_pass)
#      s.sendmail(email,to,body)
# print("otp send succesfully",otp)

'''modules ==> module is a python file 
mainly 1) in-build module 2)user define module
need ==> To increase code reusability and connect different different files to each other '''
spp=5
def output(*args):
    for i in args:
        print(i,end=" ")

