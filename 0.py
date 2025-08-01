import tkinter
from tkinter import*

t=tkinter.Tk()
t.geometry('800x800')
t.title('Dash bord')
a=Label(t,text='Employee')
a.place(x=50,y=50)
k=Button(t,text='Insert')
k.place(x=100,y=50)
k1=Button(t,text='Delete')
k1.place(x=150,y=50)
k2=Button(t,text='find')
k2.place(x=200,y=50)
k3=Button(t,text='update')
k3.place(x=250,y=50)
k4=Button(t,text='show')
k4.place(x=300,y=50)
t.mainloop()