# def atm():
#     global balance
#     global pin 
#     pin=150
#     balance=100000
#     print('''
#           press 1 for deposite
#           press 2 for chekbalance
#           press 3 for withdraw
#           press 4 for change pin''')
#     decision=int(input("enter choice : "))
#     if decision==1:
#         amount=int(input("enter amount to deposite : "))
#         deposite(amount,balance)

# def deposite(amount,balance):
#     balance+=amount
#     print(f"succesfull deposite ${amount} and you current balance is {balance}")

# def check_balance(balance):
#     print(f"you current balance is {balance}")


# def withdraw(amount,balance):
#     if amount<=balance:
#         balance-=amount
#         print(f'you withdraw the amount{amount} is succesfully and your current balance is {balance}')
#     else:
#         print("insufficiant amount")

# def change_pin(new_pin):
#     pin=new_pin

# atm()

"""ATM MACHINE"""
# from tkinter import messagebox
# def atm():
#     global balance
#     global  pin 
#     balance=10000000
#     pin=123
# atm()

# def deposite(amount):
#     global balance
#     balance+=amount
#     print(f"succesfull deposite ${amount} and you current balance is {balance}")

# def check_balance():
#     global balance
#     print(f"you current balance is {balance}")


# def withdraw(amount):
#     global balance
#     auth_pin=int(input("enter the pin : "))

#     if amount<=balance and pin==auth_pin:
#         balance-=amount
#         messagebox.showinfo("suceesful withdraw")
#         print(f'you withdraw the amount{amount} is succesfully and your current balance is {balance}')
#     else:
#         messagebox.showinfo("wrong pin")
#         print("insufficiant amount")

# def change_pin(new_pin):
#     global pin
#     pin=new_pin

# def main():
#     while True:
#         print('''
#             press 1 for deposite
#             press 2 for chekbalance
#             press 3 for withdraw
#             press 4 for change pin
#             press x for exit ''')
#         decision=int(input("enter choice : "))
#         if decision==1:
#             amount=int(input("enter amount to deposite : "))
#             deposite(amount)
#         elif decision==2:
#             check_balance()
#         elif decision==3:
#             amount=int(input("enter amount to withdraw : "))
#             withdraw(amount)
#         elif decision==4:
#             new_pin=int(input("enter new pin : "))
#             change_pin(new_pin)
#         if  decision==0:
#             break

# main()


'''ATM MACHINE USING '''
# import random
# class bank:
#     def __init__(self):
#         self.account_number=random.randint(111111111,999999999)
#         self.balance=5000
#     def withdow(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#         else:
#             print("insufficiat balance transaction failed ")
#     def deposite(self,amount):
#         self.balance+=amount
#         print("deposite succesfully")
            
# a=bank()
# print(a.account_number)
# print(a.balance)
# a.withdow(500)
# print(a.balance)
# a.deposite(500)
# print(a.balance)