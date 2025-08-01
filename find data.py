import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
t=tkinter.Tk()
t.geometry('800x800')
def finddata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='mydatabase')
    cur=db.cursor()
    xa=int(ae.get())
    sql="select name,city,salary from staff where staffid=%d"%(xa)
    cur.execute(sql)
    data=cur.fetchone()
    de.delete(0,100)
    fe.delete(0,100)
    he.delete(0,100)
    de.insert(0,data[0])
    fe.insert(0,data[1])
    he.insert(0,str(data[2]))
    db.close()
def cd():
    t.destroy()
a=Label(t,text='Staff_id',font=('algebian',12))
a.place(x=50,y=20)
ae=Entry(t,width=15)
ae.place(x=200,y=20)
btn1=Button(t,text='find',command=finddata)
btn1.place(x=150,y=60)
d=Label(t,text='Name',font=('algebian',12))
d.place(x=50,y=100)
de=Entry(t,width=15)
de.place(x=200,y=100)
f=Label(t,text='City')
f.place(x=50,y=140)
fe=Entry(t,width=15)
fe.place(x=200,y=140)
h=Label(t,text='Salary')
h.place(x=50,y=180)
he=Entry(t,width=15)
he.place(x=200,y=180)

btn3=Button(t,text='Close',command=cd)
btn3.place(x=150,y=220)






t.mainloop()
