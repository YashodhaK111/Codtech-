import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

root = tk.Tk()
root.title("To-Do List")

# Entry and Add Button
task_entry = tk.Entry(root, font="Arial 14")
task_entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", font="Arial 12", command=add_task)
add_btn.pack()

# Listbox
listbox = tk.Listbox(root, font="Arial 14", width=40, height=10)
listbox.pack(pady=10)

# Delete Button
delete_btn = tk.Button(root, text="Delete Task", font="Arial 12", command=delete_task)
delete_btn.pack()

root.mainloop()
