import tkinter
from tkinter import *
from tkinter import ttk
t=tkinter.Tk()
t.geometry('800x800')
t.title('my')
a=Label(t,text='reg form',font=('arial',20),fg='red')
a.place(x=350,y=20)
b=Label(t,text='hobbies')
b.place(x=50,y=100)
xa=IntVar()
xb=IntVar()
cr=Checkbutton(t,text='Reading',variable=xa,onvalue=1,offvalue=0)
cm=Checkbutton(t,text='music',variable=xb,onvalue=1,offvalue=0)
cr.place(x=400,y=100)
cm.place(x=500,y=100)
d=Label(t,text='hobbies')
d.place(x=50,y=140)
b=Text(t,height=3,width=50)
b.place(x=400,y=140)
pr=ttk.Progressbar(t)
pr['value']=60
pr.place(x=300,y=500)
t.mainloop()