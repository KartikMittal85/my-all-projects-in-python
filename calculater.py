import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
t=tkinter.Tk()
t.geometry('800x800')
t.title("my")
def sum():
    xa=int(ae.get())
    xb=int(be.get())
    xd=xa+xb
    messagebox.showinfo('sum',str(xd))
def sub():
    xa=int(ae.get())
    xb=int(be.get())
    xd=xa-xb
    messagebox.showinfo('sub',str(xd))
def mul():
    xa=int(ae.get())
    xb=int(be.get())
    xd=xa*xb
    messagebox.showinfo('mul',str(xd))
def div():
    xa=int(ae.get())
    xb=int(be.get())
    xd=xa/xb
    messagebox.showinfo('div',str(xd))
a=Label(t,text='No1')
a.place(x=50,y=60)
ae=Entry(t,width=20)
ae.place(x=500,y=60)
b=Label(t,text='No2')
b.place(x=50,y=100)
be=Entry(t,width=20)
be.place(x=500,y=100)
btn=Button(t,text='+',command=sum)
btn.place(x=300,y=200)
btn=Button(t,text='-',command=sub)
btn.place(x=350,y=200)
btn=Button(t,text='*',command=mul)
btn.place(x=400,y=200)
btn=Button(t,text='/',command=div)
btn.place(x=450,y=200)
t.mainloop()