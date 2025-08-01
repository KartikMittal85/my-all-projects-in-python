import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
t=tkinter.Tk()
t.geometry('800x800')
t.title("my")
def ch():
    x=int(sp.get())
    a.config(font=('arial',x))
    x=int(sc.get())
    pr['value']=x
def col():
    x=colorchooser.askcolor()
    t.config(bg=x[1])
a=Label(t,text='kartik')
a.place(x=400,y=20)
k=Label(t,text='size')
k.place(x=50,y=40)
sp=Spinbox(t,from_=1,to=100,command=ch)
sp.place(x=500,y=40)
btn=Button(t,text='colour',command=col)
btn.place(x=50,y=200)
pr=ttk.Progressbar(t)
pr.place(x=100,y=400)
t.mainloop()