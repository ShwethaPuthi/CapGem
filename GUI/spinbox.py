import tkinter as tk  

def on_spinbox_change():  
    selected_value = spinbox.get()  
    label_value.config(text=f"Selected Value: {selected_value}")  

# Create the main application window  
root = tk.Tk()  
root.title("SpinBox Example")  

# Create SpinBox widget  
spinbox = tk.Spinbox(root, from_=0, to=100, command=on_spinbox_change)  
spinbox.pack(pady=20)  

# Label to display selected value  
label_value = tk.Label(root, text="Selected Value: 0")  
label_value.pack()  

# Start the Tkinter event loop  
root.mainloop()