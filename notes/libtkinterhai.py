# '''  tkinter'''
# import tkinter as tk
# from tkinter import messagebox 
# window=tk.Tk()
# window.geometry("500x500")  # size of window 
# window.config(background='#27F59C')  # background colour of window
# label1=tk.Label(text="WELCOME TO MY FIRST APP ",font=('bold',25),bg="#27F59C")
# label1.place(x=500,y=150)
# entry1=tk.Entry(window,font=('bold',25),bg="#CFCBDA")
# entry1.place(x=500,y=200)
# entry2=tk.Entry(window,font=('bold',25),bg="#DFDAE9")
# entry2.place(x=500,y=250)

# def display():
#     print(var.get())
# var=tk.StringVar()
# radio1=tk.Radiobutton(window,text="male",variable=var,value="male",font=('bold',25),command=display)
# radio1.pack(side="top")
# radio2=tk.Radiobutton(window,text="female",variable=var,value="female",font=('bold',25),command=display)
# radio2.pack(side="top")


# def action1():
#     n1=int(entry1.get())
#     n2=int(entry2.get())
#     r=n1+n2
#     label2=tk.Label(text=f"your result is = {r}",font=('bold',25),fg="#132CD3",bg='#27F59C')
#     label2.place(x=500,y=400)

# def display():
#     print(option1.get())
#     print(option2.get())
# option1=tk.BooleanVar()
# option2=tk.BooleanVar()
# check1=tk.Checkbutton(window,text='cse',variable=option1,font=('bold',35),command=display)
# check1.pack()
# check2=tk.Checkbutton(window,text='me',variable=option2,font=('bold',35),command=display)
# check2.pack()

# button=tk.Button(text="calculate",font=('bold',30),bg='green',command=action1)
# button.place(x=700,y=300)
# window.mainloop()

# '''new data hai'''
# import tkinter as tk
# from tkinter import ttk
# n=5
# import sqlite3
# connetion=sqlite3.connect('jit.db')
# cursor=connetion.cursor()
# window=tk.Tk()
# window.geometry('800x600')

# label=tk.Label(window,text="welcome to my app",font=('bold',25))
# label.place(x=10,y=50)
# entry=tk.Entry(window,font=('bold',25),bg='white')
# entry.place(x=300,y=50)
# '''this is display function of button to call by command'''
# def display():
#     name=str(entry.get())
#     cursor.execute("create table if not exists student(id int,name varchar(20))")
#     cursor.execute("insert into student values(?,?)",(n,name))
#     connetion.commit()
# button=tk.Button(window,text="click me",font=('bold',25),bg='green',command=display)
# button.place(x=200,y=100)

# def display_select(event):
#     print(com.get())
# data=['python','c','c++','java']
# com=ttk.Combobox(window,values=data,font=('bold',25))
# com.bind("<<ComboboxSelected>>",display_select)
# com.place(x=100,y=200)

# def d(event):
#     print(event.x,event.y)

# window.bind('<B1-Motion>',d)  

# window.mainloop()
# print('success')

'''registration '''
import tkinter as tk
import sqlite3
from tkinter import messagebox

w1=tk.Tk()
w1.geometry("600x800")
w1.config(bg="white")

label1=tk.Label(w1,text="user name",font=("bold",25))
label1.place(x=10,y=50)
entry1=tk.Entry(w1,font=('bold',25),bg='pink')
entry1.place(x=200,y=50)

label2=tk.Label(w1,text="password",font=("bold",25))
label2.place(x=10,y=100)
entry2=tk.Entry(w1,font=('bold',25),bg='pink')
entry2.place(x=200,y=100)

label3=tk.Label(w1,text="email",font=("bold",25))
label3.place(x=10,y=150)
entry3=tk.Entry(w1,font=('bold',25),bg='pink')
entry3.place(x=200,y=150)

def save():
    name=entry1.get()
    password=entry2.get()
    email=entry3.get()
button1=tk.Button(w1,text="register",font=('bold',25),bg="green",command=save)
button1.place(x=150,y=200)

w1.mainloop()
