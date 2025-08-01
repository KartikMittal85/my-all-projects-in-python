import tkinter
from tkinter import *
from tkinter import ttk
t=tkinter.Tk()
t.geometry('800x800')
t.title("my")
tt=0
qt=0
def cal():
    xa=int(be.get())
    xb=int(ce.get())
    global tt
    tt=xa*xb
    bte1.delete(0,100)
    bte1.insert(0,str(tt))
def gst():
    global tt
    global gt
    gt=tt*0.18
    bte2.delete(0,100)
    bte2.insert(0,str(gt))
def ft():
    global tt
    global gt
    fa=tt+gt
    btne3.delete(0,100)
    btne3.insert(0,str(fa))
a=Label(t,text='name')
a.place(x=50,y=60)
ae=Entry(t,width=20)
ae.place(x=500,y=60)
b=Label(t,text='price')
b.place(x=50,y=100)
be=Entry(t,width=20)
be.insert(0,'0')
be.place(x=500,y=100)
c=Label(t,text='qty')
c.place(x=50,y=140)
ce=Spinbox(t,from_=1,to=100)
ce.place(x=500,y=140)
btn1=Button(t,text='total',command=cal)
btn1.place(x=50,y=180)
bte1=Entry(t,width=20)
bte1.insert(0,'0')
bte1.place(x=500,y=180)
btn2=Button(t,text='gst',command=gst)
btn2.place(x=50,y=220)
bte2=Entry(t,width=20)
bte2.insert(0,'0')
bte2.place(x=500,y=220)
btn3=Button(t,text='find',command=ft)
btn3.place(x=50,y=260)
btne3=Entry(t,width=20)
btne3.insert(0,'0')
btne3.place(x=500,y=260)
t.mainloop()