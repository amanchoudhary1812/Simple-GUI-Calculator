import tkinter as tk

# Function definitions for calculator operations 
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def all_clear():
    entry.delete(0, tk.END)

def delete_last():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Setting up main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("420x520")  # Slightly larger to accommodate border padding
root.config(bg="#121212")  # Dark theme background color

# Digital display for calculator
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=0, relief='flat', justify='right', fg="#ffffff", bg="#222222")
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=(20, 10))

# Adding AC and DEL buttons at the top
top_buttons = [
    ('AC', 1, 0), ('DEL', 1, 3)
]

for (text, row, col) in top_buttons:
    action = all_clear if text == 'AC' else delete_last
    button = tk.Button(root, text=text, command=action, font=('Arial', 18), fg="#000000", bg="#ffffff", padx=20, pady=20)
    button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

# Calculator main buttons
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('C', 5, 0), ('0', 5, 1), ('=', 5, 2), ('+', 5, 3)
]

# Adding main buttons to the grid with padding around buttons and borders
for (text, row, col) in buttons:
    action = lambda x=text: button_click(x) if x not in ['=', 'C'] else None
    if text == 'C':
        action = clear_entry
    elif text == '=':
        action = evaluate
    button = tk.Button(root, text=text, command=action, font=('Arial', 18), fg="#000000", bg="#ffffff", padx=20, pady=20)
    button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

# Configure grid layout to scale with window size and add padding around the edges
for i in range(6):
    root.grid_rowconfigure(i, weight=1, minsize=60)
    if i < 4:
        root.grid_columnconfigure(i, weight=1, minsize=60)

root.mainloop()
