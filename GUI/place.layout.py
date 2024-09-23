import tkinter as tk
from tkinter import PhotoImage
import tkinter as tk
root=tk.Tk()
root.title=("Place layout")
icon=PhotoImage(file="C:\\Users\\shwet\\Desktop\\CapGem\\GUI\\images.png")
root.iconphoto(True,icon)
root.geometry("400x300")
label1=tk.Label(root,text="Blue",bg="blue")
label1.place(x=50,y=50)
label2=tk.Label(root,text="Red",bg="red")
label2.place(x=100,y=100)
label3=tk.Label(root,text="Pink",bg="pink")
label3.place(x=150,y=150)
root.mainloop()