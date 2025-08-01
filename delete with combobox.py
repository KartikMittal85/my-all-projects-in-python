import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
t=tkinter.Tk()
t.geometry('800x800')
xt=[]
def filldata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='mydatabase')
    cur=db.cursor() 
    sql="select staffid from staff"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        xt.append(res[0])
    db.close()
def deletedata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='mydatabase')
    cur=db.cursor()
    xa=int(ae.get())
    sql="delete from staff where staffid=%d"%(xa)
    cur.execute(sql)
    ae.delete(0,100)
    messagebox.showinfo('hi','delete')
    db.commit()
    db.close()
def cd():
    t.destroy()
a=Label(t,text='Staff_id')
a.place(x=50,y=20)
ae=ttk.Combobox(t,width=15)
filldata()
ae['values']=xt
ae.place(x=200,y=20)
btn1=Button(t,text='Delete',command=deletedata)
btn1.place(x=150,y=60)
t.mainloop()