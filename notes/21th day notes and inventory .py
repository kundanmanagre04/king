'''inheritance => super(parents) class ki properties ko base(child) class me inherit karna its called inheritance '''
'''1)single 2)multipal 1)multipal downword 2)multipal upword 3)multilevel 4) hyrachical 5)hybrid inheritance '''
'''single level inheritance '''
# class c1:
#     data=90
#     def m1(self):
#         print("i am m1 from c1 ")
# class c2(c1):
#     name="kundan"
# obj=c2()
# print(obj.data)
# obj.m1()
# print(obj.name)

# class above_18:
#     voter_id=1234
#     def going_office(self):
#         print("working in office")
#     def play(self):
#         print("playing cricket")

# class below_18(above_18):
#     def eating(self):
#         print("eating food")
#     def play(self):
#         print("playing chess")
#         # super().play()
#         above_18.play(self)
# a=below_18()
# a.play()

'''inventory managment project'''
class ims:
    def __init__(self):
        self.product_name=[]
        self.quantity=[]
        self.price=[]
        self.qua_pri=[]
    def add(self,p_name,p_quantity,p_price):
        self.product_name.append(p_name)
        self.quantity.append(p_quantity)
        self.price.append(p_price)
        self.qua=dict(zip(["quantity","price"],[p_quantity,p_price]))
        self.qua_pri.append(self.qua)
        self.data=dict(zip(self.product_name,self.qua_pri))
    def display_record(self):
        print(self.data)  
    def buy(self,p_name,p_quantity):
        print(self.data)
obj=ims()
while True:
    product=input("enter a product name : ")
    quantity=int(input("enter the quantity : "))    
    price=int(input("enter a price of product : "))
    obj.add(product,quantity,price)
    choice=input("press Y to enter more items\n press N to exit ")
    if choice=='N' or choice=='n':
        break
obj.display_record()
obj.display_record()









