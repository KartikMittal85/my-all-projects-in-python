import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
t=tkinter.Tk()
t.geometry('800x800')
t.title("my")
def hello():
    messagebox.showinfo('hi','welcome')
btn=Button(t,text='hello',command=hello)
btn.place(x=300,y=200)
t.mainloop()