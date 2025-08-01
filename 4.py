import tkinter
from tkinter import *
from tkinter import ttk
t=tkinter.Tk()
t.geometry('800x800')
t.title("my")
xp=IntVar()
r1=Radiobutton(t,text='red',variable=xp,value=1)
r2=Radiobutton(t,text='green',variable=xp,value=0)
r3=Radiobutton(t,text='blue',variable=xp,value=1)
r1.place(x=350,y=60)
r2.place(x=350,y=100)
r3.place(x=350,y=140)
t.mainloop()