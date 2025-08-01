import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
t=tkinter.Tk()
t.geometry('800x800')
def savedata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='mydatabase')
    cur=db.cursor()
    xa=int(ae.get())
    xb=de.get()
    xc=fe.get()
    xd=int(he.get())
    sql="insert into staff values(%d,'%s','%s',%d)"%(xa,xb,xc,xd)
    cur.execute(sql)
    db.commit()
    ae.delete(0,100)
    de.delete(0,100)
    fe.delete(0,100)
    he.delete(0,100)
    db.close()
    messagebox.showinfo('hi','save')
def cd():
    t.destroy()
a=Label(t,text='Staff_id')
a.place(x=50,y=20)
ae=Entry(t,width=15)
ae.place(x=200,y=20)
d=Label(t,text='Name')
d.place(x=50,y=60)
de=Entry(t,width=15)
de.place(x=200,y=60)
f=Label(t,text='City')
f.place(x=50,y=100)
fe=Entry(t,width=15)
fe.place(x=200,y=100)
h=Label(t,text='Salary')
h.place(x=50,y=140)
he=Entry(t,width=15)
he.place(x=200,y=140)
btn1=Button(t,text='Save',command=savedata)
btn1.place(x=50,y=200)
btn2=Button(t,text='Close',command=cd)
btn2.place(x=200,y=200)






t.mainloop()
