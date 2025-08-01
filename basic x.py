import tkinter
from tkinter import *
t=tkinter.Tk()
t.geometry('800x800')
t.title('my')
a=Canvas(t,height=700,width=700,bg='pink')
a.place(x=10,y=10)
a.create_rectangle(50,250,300,350,fill='orange')
a.create_oval(300,50,500,250,fill='orange')
p=[100,500,250,350,400,500]
a.create_polygon(p,fill='green',outline='red',width=4) 
a.create_text(300,400,text='testing')
t.mainloop()