import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
t=tkinter.Tk()
t.geometry('800x800')
t.title("my")
def cal():
    xa=int(be.get())
    xb=int(ce.get())
    xc=int(de.get())
    xd=int(ee.get())
    global tt
    tt=xa+xb+xc+xd
    btne1.delete(0,100)
    btne1.insert(0,str(tt))
def par():
    global tt
    global gt
    gt=tt/400*100
    btne2.delete(0,100)
    btne2.insert(0,str(gt))
a=Label(t,text='name')
a.place(x=50,y=60)
ae=Entry(t,width=20)
ae.place(x=500,y=60)
b=Label(t,text='sem1')
b.place(x=50,y=100)
be=Entry(t,width=20)
be.place(x=500,y=100)
c=Label(t,text='sem2')
c.place(x=50,y=140)
ce=Entry(t,width=20)
ce.place(x=500,y=140)
d=Label(t,text='sem3')
d.place(x=50,y=180)
de=Entry(t,width=20)
de.place(x=500,y=180)
e=Label(t,text='sem4')
e.place(x=50,y=220)
ee=Entry(t,width=20)
ee.place(x=500,y=220)
btn1=Button(t,text='total',command=cal)
btn1.place(x=50,y=280)
btne1=Entry(t,width=20)
btne1.place(x=500,y=280)
btn2=Button(t,text='par',command=par)
btn2.place(x=50,y=320)
btne2=Entry(t,width=20)
btne2.place(x=500,y=320)
btn3=Button(t,text='grade')
btn3.place(x=50,y=360)
btne3=Entry(t,width=20)
btne3.place(x=500,y=360)
t.mainloop()