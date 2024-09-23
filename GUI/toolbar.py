import tkinter as tk  

# Create a new file  
def new_file():  
    print("New file created")  

# Open a file  
def open_file():  
    print("File opened")  

# Save a file  
def save_file():  
    print("File saved")  

# Create the root window  
root = tk.Tk()  
root.title("Toolbar Example")  
root.geometry("400x300")  

# Create a frame for the toolbar  
toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)  
toolbar.pack(side=tk.TOP, fill=tk.X)  

# Create and add buttons to the toolbar  
new_button = tk.Button(toolbar, text="New", command=new_file)  
new_button.pack(side=tk.LEFT, padx=2, pady=2)  

open_button = tk.Button(toolbar, text="Open", command=open_file)  
open_button.pack(side=tk.LEFT, padx=2, pady=2)  

save_button = tk.Button(toolbar, text="Save", command=save_file)  
save_button.pack(side=tk.LEFT, padx=2, pady=2)  

# Start the main event loop  
root.mainloop()