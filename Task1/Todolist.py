import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def remove_task():
    try:
        listbox_tasks.delete(tk.ACTIVE)
    except tk.TclError:
        pass

def edit_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        updated_task = entry_task.get()
        if updated_task:
            listbox_tasks.delete(selected_index)
            listbox_tasks.insert(selected_index, updated_task)
            entry_task.delete(0, tk.END)
    except IndexError:
        pass

root = tk.Tk()
root.title("To-Do List")

header_frame = tk.Frame(root, bg="green", padx=10, pady=5)
header_frame.pack(fill=tk.X)

header_label = tk.Label(header_frame, text="To-Do List", fg="white", bg="green", font=("Helvetica", 16, "bold"))
header_label.pack()

frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks, orient=tk.VERTICAL, command=listbox_tasks.yview)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)

entry_task = tk.Entry(root, width=50)
entry_task.pack()

button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_remove_task = tk.Button(root, text="Remove Task", width=48, command=remove_task)
button_remove_task.pack()

button_edit_task = tk.Button(root, text="Edit Task", width=48, command=edit_task)
button_edit_task.pack()

root.mainloop()
