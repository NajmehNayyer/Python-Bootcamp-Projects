import tkinter as tk

FONT = ("New Roman Times", 10, "normal")

def convert():
    equation = float(num_input.get()) * 1.6
    new_num_output = int(round(equation, 0))
    num_output.config(text=new_num_output)


# Create the window and paddings
my_window = tk.Tk()
my_window.title("Mile to Km Converter")
my_window.geometry("300x115")
my_window.config(padx=55, pady=20)

# Entry of number
num_input = tk.Entry(width=10, font=FONT)
num_input.grid(column=1, row=0)

# Scale of entry value
inp_scale = tk.Label(text=" Miles", font=FONT)
inp_scale.grid(column=2, row=0)

# Is equal
is_equal = tk.Label(text="is equal to", font=FONT)
is_equal.grid(column=0, row=1)

# Converted value
num_output = tk.Label(text="0", font=FONT)
num_output.grid(column=1, row=1)

# Scale of output value
out_scale = tk.Label(text="Km", font=FONT)
out_scale.grid(column=2, row=1)

# Calculate function
cal_but = tk.Button(text="Calculate", command=convert, font=FONT)
cal_but.grid(column=1, row=2)

my_window.mainloop()
