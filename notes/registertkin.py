import tkinter as tk
import sqlite3
connection=sqlite3.connect("student.db")
cursor=connection.cursor()
from tkinter import ttk
window=tk.Tk()
window.geometry('800x600')
window.config(bg='white')
label1=tk.Label(window,text="NAME",font=('bold',25))
label1.place(x=10,y=50)
entry1=tk.Entry(window,font=('bold',25),bg='red')
entry1.place(x=250,y=50)

label2=tk.Label(window,text="ENROLL.NO",font=('bold',25))
label2.place(x=10,y=100)
entry2=tk.Entry(window,font=('bold',25),bg='red')
entry2.place(x=250,y=100)

label3=tk.Label(window,text="COURSE",font=('bold',25))
label3.place(x=10,y=150)

data=['B.TACH','ME','CIVIL']
com1=ttk.Combobox(window,values=data,font=('bold',25))
com1.bind("<<ComboboxSelected>>")
com1.place(x=250,y=150)

label4=tk.Label(window,text="BRANCH",font=('bold',25))
label4.place(x=10,y=200)

data=['CSE','AI','DS']
com2=ttk.Combobox(window,values=data,font=('bold',25))
com2.bind("<<ComboboxSelected>>")
com2.place(x=250,y=200)

label5=tk.Label(window,text="GENDER",font=('bold',25))
label5.place(x=10,y=250)

var=tk.StringVar()
radio1=tk.Radiobutton(window,text="male",variable=var,value="male",font=('bold',25))
radio1.place(x=200,y=250)
radio2=tk.Radiobutton(window,text="female",variable=var,value="female",font=('bold',25))
radio2.place(x=400,y=250)

def show():
    name=entry1.get()
    en=entry2.get()
    br=com1.get()
    co=com2.get()
    gen=var.get()
    cursor.execute("create table if not exists student(name varchar(20),enroll int,course varchar(20), branch varchar(20),gender varcahr(20))")
    cursor.execute("insert into student values(?,?,?,?,?)",(name,en,br,co,gen))
    connection.commit()

    
button=tk.Button(window,text="SUBMIT",font=('bold',25),bg='green',command=show)
button.place(x=300,y=300)

window.mainloop()
connection.close()

'''python file ko single file running file me badalta hai'''
''''pip install pyinstaller
# pyinstaller --onefile file name'''