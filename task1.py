import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        temperature_input = float(entry.get())
        original_unit = combo_box_from.get()

        if original_unit == 'C':
            celsius = temperature_input
            fahrenheit = (celsius * 9/5) + 32
            kelvin = celsius + 273.15
        elif original_unit == 'F':
            fahrenheit = temperature_input
            celsius = (fahrenheit - 32) * 5/9
            kelvin = (fahrenheit + 459.67) * 5/9
        elif original_unit == 'K':
            kelvin = temperature_input
            celsius = kelvin - 273.15
            fahrenheit = (kelvin * 9/5) - 459.67
        else:
            result_var.set("Invalid unit. Please enter C, F, or K.")
            return

        result_var.set(
            f"Original Temperature: {temperature_input} {original_unit}\n"
            f"Converted to Celsius: {celsius:.2f} C\n"
            f"Converted to Fahrenheit: {fahrenheit:.2f} F\n"
            f"Converted to Kelvin: {kelvin:.2f} K"
        )
    except ValueError:
        result_var.set("Invalid temperature value. Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")

# Input widgets
frame_input = ttk.Frame(root, padding="10")
frame_input.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_temperature = ttk.Label(frame_input, text="Enter Temperature:")
label_temperature.grid(row=0, column=0, pady=(0, 5))

entry = ttk.Entry(frame_input)
entry.grid(row=0, column=1, pady=(0, 5))

label_unit_from = ttk.Label(frame_input, text="From:")
label_unit_from.grid(row=1, column=0, pady=(0, 5))

combo_box_from = ttk.Combobox(frame_input, values=["C", "F", "K"])
combo_box_from.grid(row=1, column=1, pady=(0, 5))
combo_box_from.set("C")

# Result display
result_var = tk.StringVar()
label_result = ttk.Label(frame_input, textvariable=result_var, wraplength=300)
label_result.grid(row=2, column=0, columnspan=2, pady=(10, 0))

# Conversion button
button_convert = ttk.Button(frame_input, text="Convert", command=convert_temperature)
button_convert.grid(row=3, column=0, columnspan=2, pady=(10, 0))

# Run the GUI
root.mainloop()
