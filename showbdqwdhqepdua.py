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
    sql="select productid,catid,pname,price,unit,qty from products"
    cur.execute(sql)
    data=cur.fetchall()
    global i
    for res in data:
        aa.append(res[0])
        ab.append(res[1])
        ac.append(res[2])
        ad.append(res[3])
        ae.append(res[4])
        af.append(res[5])
    db.close()
def firstrecord():
    global i
    i=0
    b.delete(0,100)
    d.delete(0,100)
    f.delete(0,100)
    h.delete(0,100)
    beie.delete(0,100)
    xee.delete(0,100)
    b.insert(0,aa[i])
    d.insert(0,ab[i])
    f.insert(0,ac[i])
    h.insert(0,ad[i])
    beie.insert(0,ae[i])
    xee.insert(0,af[i])
def nextrecord():
    global i
    i=i+1
    b.delete(0,100)
    d.delete(0,100)
    f.delete(0,100)
    h.delete(0,100)
    beie.delete(0,100)
    xee.delete(0,100)
    b.insert(0,aa[i])
    d.insert(0,ab[i])
    f.insert(0,ac[i])
    h.insert(0,ad[i])
    beie.insert(0,ae[i])
    xee.insert(0,af[i])
def prevrecord():
    global i
    i=i-1
    b.delete(0,100)
    d.delete(0,100)
    f.delete(0,100)
    h.delete(0,100)
    beie.delete(0,100)
    xee.delete(0,100)
    b.insert(0,aa[i])
    d.insert(0,ab[i])
    f.insert(0,ac[i])
    h.insert(0,ad[i])
    beie.insert(0,ae[i])
    xee.insert(0,af[i])
def lastrecord():
    global i
    i=len(aa)-1
    b.delete(0,100)
    d.delete(0,100)
    f.delete(0,100)
    h.delete(0,100)
    beie.delete(0,100)
    xee.delete(0,100)
    b.insert(0,aa[i])
    d.insert(0,ab[i])
    f.insert(0,ac[i])
    h.insert(0,ad[i])
    beie.insert(0,ae[i])
    xee.insert(0,af[i])

a=Label(t,text='productid')
a.place(x=20,y=50)
b=Entry(t,width=30)
b.place(x=500,y=50)
c=Label(t,text='category id')
c.place(x=20,y=150)
d=Entry(t,width=30)
d.place(x=500,y=150)
e=Label(t,text='product name')
e.place(x=20,y=200)
f=Entry(t,width=30)
f.place(x=500,y=200)
g=Label(t,text='price')
g.place(x=20,y=250)
h=Entry(t,width=30)
h.place(x=500,y=250)
bei=Label(t,text='unit')
bei.place(x=20,y=290)
beie=Entry(t,width=20)
beie.place(x=500,y=290)
x=Label(t,text='qty')
x.place(x=20,y=340)
xee=Entry(t,width=10)
xee.place(x=500,y=340)
k=Button(t,text='First',command=firstrecord)
k.place(x=100,y=400)
n=Button(t,text='Next',command=nextrecord)
n.place(x=200,y=400)
p=Button(t,text='Previous',command=prevrecord)
p.place(x=300,y=400)
r=Button(t,text='Last',command=lastrecord)
r.place(x=400,y=400)
filldata()
t.mainloop()