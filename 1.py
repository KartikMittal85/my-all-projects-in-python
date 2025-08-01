import tkinter
from tkinter import *
from tkinter import ttk
t=tkinter.Tk()
t.geometry('800x800')
t.title("my")
def chred():
    t.config(bg='red')
def chgreen():
    t.config(bg='green')
def chblue():
    t.config(bg='blue')
btn1=Button(t,text='red',command=chred)
btn1.place(x=300,y=200)
btn2=Button(t,text='blue',command=chblue)
btn2.place(x=300,y=300)
btn3=Button(t,text='green',command=chgreen)
btn3.place(x=300,y=400)
t.mainloop()