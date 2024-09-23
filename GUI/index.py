# #import tkinter as tk
# #create the main window
# #root=tk.Tk()
# #root.title("Hello, this is a simple GUI Program using Tkinter")
# #root.geometry("300x200")
# #root.mainloop()

# import tkinter as tk
# from tkinter import PhotoImage
# root=tk.Tk()
# root.title=("My app")
# icon=PhotoImage(file="C:\\Users\\shwet\\Desktop\\CapGem\\GUI\\images.png")
# root.iconphoto(True,icon)
# root.geometry("400x300")
# root.mainloop()

import tkinter as tk
root=tk.Tk()
root.geometry("300x200")
label1=tk.Label(root,text="Blue",bg="blue")
label1.pack(fill=tk.BOTH,expland=True)
label2=tk.Label(root,text="Red",bg="red")
label2.pack(fill=tk.BOTH,expland=True)
root.mainloop()