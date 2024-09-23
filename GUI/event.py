import tkinter as tk  

def on_key_press(event):  
    # Get the current contents of the entry widget  
    current_text = entry.get()  
    print(f"Current Text: {current_text}")  

def on_entry_focus_in(event):  
    print("Entry Widget Focused")  

# Create the main application window  
root = tk.Tk()  
root.title("Event Handling Example")  

# Create an entry widget  
entry = tk.Entry(root, width=30)  
entry.pack(pady=20, padx=50)  

# Bind events to entry widget  
entry.bind('<Key>', on_key_press)  # Key press event  
entry.bind('<FocusIn>', on_entry_focus_in)  # Focus in event  

# Run the main event loop  
root.mainloop()