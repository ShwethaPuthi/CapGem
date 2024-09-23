import tkinter as tk
root=tk.Tk()
root.geometry("300x200")
label1=tk.Label(root,text="Red",bg="red")
label1.pack(fill=tk.BOTH,expand=True)
label2=tk.Label(root,text="Yellow",bg="yellow")
label2.pack(fill=tk.BOTH,expand=True)
root.mainloop()