import tkinter as tk  
import tkinter.messagebox as mb  

def show_message():  
    mb.showinfo(title="Message", message="Hello, Tkinter!")  

root = tk.Tk()  
root.title("MessegeBox Example")  
root.geometry("400x200")  

tk.Button(root, text="Show Message", command=show_message).pack(pady=20)  
root.mainloop()