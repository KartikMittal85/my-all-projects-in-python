import tkinter
from tkinter import *
t=tkinter.Tk()
t.geometry('800x800')
t.title('my')
a=Canvas(t,height=700,width=700,bg='white')
a.place(x=10,y=10)
a.create_rectangle(20,20,300,50,fill='orange')
a.create_rectangle(20,80,300,50,fill='white')
a.create_oval(150,57,170,76,fill='blue')
a.create_rectangle(20,110,300,80,fill='lightgreen')
a.create_rectangle(20,10,10,400,fill='brown')
a.create_text(200,300,text='INDIA')


#STAR
a.create_line(55,15,25,60)
a.create_line(25,60,90,30)
a.create_line(55,15,85,60)
a.create_line(85,60,20,30)
a.create_line(20,30,90,30)
#d.create_line(150,30,30,30)

t.mainloop()