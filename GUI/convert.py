import tkinter as tk  
def convert():  
    try:  
        fahrenheit = float(entry.get())  
        celsius = (fahrenheit - 32) * 5/9  
        result_label.config(text=f"{fahrenheit}°F = {celsius:.2f}°C")  
    except ValueError:  
        result_label.config(text="Invalid input")
root = tk.Tk()  
root.title("Temperature Converter")  

# Labels and Entry using grid layout  
label_fahrenheit = tk.Label(root, text="Enter Fahrenheit:")  
label_fahrenheit.grid(row=0, column=0, padx=10, pady=10)  

entry = tk.Entry(root, width=10)  
entry.grid(row=0, column=1, padx=10, pady=10)  

# Convert button  
convert_button = tk.Button(root, text="Convert", command=convert)  
convert_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)  

# Result label  
result_label = tk.Label(root, text="")  
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)  

root.mainloop()