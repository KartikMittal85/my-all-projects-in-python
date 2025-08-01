import tkinter
from tkinter import *
from tkinter import ttk
t=tkinter.Tk()
t.geometry('800x800')
t.title("my")
j=Label(t,text='color')
j.place(x=50,y=60)
ct=ttk.Combobox(t)
ct['values']=['red','blue','green']
ct.place(x=500,y=60)
btn=Button(t,text='change')
btn.place(x=300,y=200)
t.mainloop()