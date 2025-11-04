'''DATABASE '''
'''data => it is row fact , figure , is data'''
'''row data => unprocessed data is called row data'''           
'''ETL(Extract, Transform, and Load)'''
'''SQL(structure query language) => its is a software that manage DBMS '''
import sqlite3
connection=sqlite3.connect("jit.db")  #JIT is name of data base

cursor=connection.cursor()
cursor.execute("create table if not exists student(id int,name varchar(20))")
cursor.execute("insert into student values(2,'virat'),(3,'aayush'),(4,'kapil')")

id=5
name="ram"
cursor.execute("insert into student values(?,?)",(id,name))

connection.commit()    # permanent data store karne ke liye

connection.close()  # close the data base


