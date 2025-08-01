import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
t=tkinter.Tk()
t.geometry('800x800')
t.title('Data Show')
aa=[]
ab=[]
ac=[]
ad=[]
ae=[]
af=[]
i=0
def filldata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='testdb')
    cur=db.cursor()
    sql="select catid,catname,discription from productcategory"
    cur.execute(sql)
    data=cur.fetchall()
    global i
    for res in data:
        aa.append(res[0])
        ab.append(res[1])
        ac.append(res[2])
    db.close()
def firstrecord():
    global i
    i=0
    b.delete(0,100)
    d.delete(0,100)
    f.delete(0,100)
    b.insert(0,aa[i])
    d.insert(0,ab[i])
    f.insert(0,ac[i])
def nextrecord():
    global i
    i=i+1
    b.delete(0,100)
    d.delete(0,100)
    f.delete(0,100)
    b.insert(0,aa[i])
    d.insert(0,ab[i])
    f.insert(0,ac[i])
def prevrecord():
    global i
    i=i-1
    b.delete(0,100)
    d.delete(0,100)
    f.delete(0,100)
    b.insert(0,aa[i])
    d.insert(0,ab[i])
    f.insert(0,ac[i])
def lastrecord():
    global i
    i=len(aa)-1
    b.delete(0,100)
    d.delete(0,100)
    f.delete(0,100)
    b.insert(0,aa[i])
    d.insert(0,ab[i])
    f.insert(0,ac[i])

a=Label(t,text='category id')
a.place(x=20,y=50)
b=Entry(t,width=30)
b.place(x=500,y=50)
c=Label(t,text='category Name')
c.place(x=20,y=150)
d=Entry(t,width=30)
d.place(x=500,y=150)
e=Label(t,text='discription')
e.place(x=20,y=200)
f=Entry(t,width=30)
f.place(x=500,y=200)
k=Button(t,text='First',command=firstrecord)
k.place(x=100,y=270)
n=Button(t,text='Next',command=nextrecord)
n.place(x=200,y=270)
p=Button(t,text='Previous',command=prevrecord)
p.place(x=300,y=270)
r=Button(t,text='Last',command=lastrecord)
r.place(x=400,y=270)
filldata()
t.mainloop()