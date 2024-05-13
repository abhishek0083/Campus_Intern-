import tkinter as tk

def button_click(number):
    current = entry_box.get()
    entry_box.delete(0, tk.END)
    entry_box.insert(0, str(current) + str(number))

def button_clear():
    entry_box.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry_box.get())
        entry_box.delete(0, tk.END)
        entry_box.insert(0, result)
    except:
        entry_box.delete(0, tk.END)
        entry_box.insert(0, "Error")
        raise

root = tk.Tk()
root.title("Calculator")
root.configure(background='#f0f0f0')  
entry_box = tk.Entry(root, width=35, borderwidth=5)
entry_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
buttons = [
    ("1", 0, 0), ("2", 0, 1), ("3", 0, 2), ("+", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("-", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("0", 3, 0), ("C", 3, 1), ("=", 3, 2), ("/", 3, 3),
    (".", 4, 0), ("(", 4, 1), (")", 4, 2), ("^", 4, 3)
]
for button_text, row, column in buttons:
    button = tk.Button(root, text=button_text, padx=40, pady=20, command=lambda button_text=button_text: button_click(button_text))
    button.grid(row=row+1, column=column, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", padx=78, pady=20, command=button_clear)
clear_button.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

equal_button = tk.Button(root, text="=", padx=86, pady=20, command=button_equal)
equal_button.grid(row=5, column=3, padx=5, pady=5)

entry_box.config(highlightbackground="#4CAF50", highlightthickness=2)

root.mainloop()
