import tkinter
from tkinter import *
t=tkinter.Tk()
t.geometry('800x800')
def cd():
    t.destroy()
a=Label(t,text='Staff_id',fg='blue',font=('alrebian',12))
a.place(x=50,y=20)
b=Entry(t,width=15)
b.place(x=200,y=20)
btn1=Button(t,text='find',fg='blue',bg='yellow',font=('algerian',12))
btn1.place(x=150,y=60)
d=Label(t,text='New_name',fg='blue',font=('algebian',12))
d.place(x=50,y=100)
e=Entry(t,width=15)
e.place(x=200,y=100)
f=Label(t,text='New_City',fg='blue',font=('algebian',12))
f.place(x=50,y=140)
g=Entry(t,width=15)
g.place(x=200,y=140)
h=Label(t,text='New_Salary',fg='blue',font=('algebian',12))
h.place(x=50,y=180)
j=Entry(t,width=15)
j.place(x=200,y=180)
btn2=Button(t,text='update',fg='green',bg='yellow',font=('algebian',12))
btn2.place(x=50,y=220)
btn3=Button(t,text='Close',fg='green',bg='yellow',font=('algebian',12),command=cd)
btn3.place(x=200,y=220)






t.mainloop()
