import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
t=tkinter.Tk()
t.geometry('800x800')
t.title("my")
def login():
    x=b.get()#name
    y=d.get()#password
    if x=='text'and y=='123':
        messagebox.showinfo('hi','sucess')
    else:
        messagebox.showinfo('hi','failed')
def cts():
    t.destroy()
a=Label(t,text='name')
a.place(x=50,y=60)
b=Entry(t,width=20)
b.place(x=500,y=60)
c=Label(t,text='password')
c.place(x=50,y=100)
d=Entry(t,width=20)
d.place(x=500,y=100)
btn1=Button(t,text='Login',command=login)
btn1.place(x=300,y=200)
btn2=Button(t,text='cancel',command=cts)
btn2.place(x=400,y=200)
t.mainloop()