import tkinter as tk  

root = tk.Tk()  
root.title("Example - add image to GUI")  

# Load and display an image  
photo = tk.PhotoImage(file=r'C:\Users\shwet\Desktop\CapGem\GUI\images.png')  
label = tk.Label(root, image=photo)  
label.pack()  

root.mainloop()