import tkinter 
from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
t=tkinter.Tk()
t.geometry('800x800')
t.title('stinkit')
am=[]
def filldata():
    bd=pymysql.connect(host='localhost',user='root',password='root',database='testbd')
    cur=bd.cursor()
    sql="select empno from employee"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        am.append(res[0])
    bd.close()
def finddata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='testbd')
    cur=db.cursor()
    xa=int(d1.get())
    sql="select name,city,salary from employee where  empno=%d"%(xa)
    cur.execute(sql)
    data = cur.fetchone()
    d2.insert(0,data[0])
    d3.insert(0,data[1])
    d4.insert(0,str(data[2]))
    db.close()
def ndata():
    d1.delete(0,100)
    d2.delete(0,100)
    d3.delete(0,100)
    d4.delete(0,100)
def close():
    t.destroy()
b1=Label(t,text='empno')
b1.place(x=50,y=60)
d1=ttk.Combobox(t,width=20)

filldata()
d1['values']=am
d1.place(x=500,y=60)
btn=Button(t,text='find',command=finddata)
btn.place(x=50,y=100)
b2=Label(t,text='name')
b2.place(x=50,y=140)
d2=Entry(t,width=20)
d2.place(x=500,y=140)
b3=Label(t,text='city')
b3.place(x=50,y=180)
d3=Entry(t,width=20)
d3.place(x=500,y=180)
b4=Label(t,text='salery')
b4.place(x=50,y=220)
d4=Entry(t,width=20)
d4.place(x=500,y=220)
btn2=Button(t,text='close',command=close)
btn2.place(x=50,y=260)
t.mainloop()