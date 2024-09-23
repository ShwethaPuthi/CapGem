import tkinter as tk
from tkinter import PhotoImage
import tkinter as tk
root=tk.Tk()
root.title=("My app")
icon=PhotoImage(file="C:\\Users\\shwet\\Desktop\\CapGem\\GUI\\images.png")
root.iconphoto(True,icon)
root.geometry("400x300")
label1=tk.Label(root,text="Blue",bg="blue")
label1.grid(row=0,column=0)
label2=tk.Label(root,text="Red",bg="red")
label2.grid(row=1,column=1)
label3=tk.Label(root,text="Pink",bg="pink")
label3.grid(row=2,column=2)
root.mainloop()