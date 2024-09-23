import tkinter as tk  

root = tk.Tk()  
root.title("Box - Example")  

canvas = tk.Canvas(root, width=400, height=400)  
canvas.pack()  

canvas.create_rectangle(50, 50, 200, 200, outline="black", fill="yellow", width=2)  

root.mainloop()