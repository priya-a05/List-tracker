import tkinter as tk
root = tk.Tk()
root.geometry("600x400")

title_label = tk.Label(root, text="List tracker", font=("Arial", 16, "bold"), bg="#d29d8f")
title_label.pack(pady=10)


root.title("List tracker")
# input box
root.configure(bg="#DCCCF7")
task_entry = tk.Entry(root, width=80)
task_entry.pack()

def add_task():
    ...

task_entry.bind("<Return>", lambda event: add_task())

# function to add task
def add_task():
    if task_entry.get().strip() == "":        return
    task = task_entry.get()
    listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)

# button
add_button = tk.Button(root, text="Save Task", command=add_task)
add_button.pack(pady=5)

# list to show tasks
listbox = tk.Listbox(root, width=80)
listbox.pack(pady=10)

#priority function
def set_priority():
    selected_task = listbox.curselection()
    if not selected_task:
        return
    priority_window = tk.Toplevel(root)
    priority_window.title("Set Priority")
    priority_window.geometry("200x150")

    def set_high():
        listbox.itemconfig(selected_task, bg="#FF6347")  # Red for high priority
        priority_window.destroy()

    def set_medium():
        listbox.itemconfig(selected_task, bg="#FFD700")  # Yellow for medium priority
        priority_window.destroy()

    def set_low():
        listbox.itemconfig(selected_task, bg="#90EE90")  # Green for low priority
        priority_window.destroy()


    high_button = tk.Button(priority_window, text="High", command=set_high)
    high_button.pack(pady=5)

    medium_button = tk.Button(priority_window, text="Medium", command=set_medium)
    medium_button.pack(pady=5)

    low_button = tk.Button(priority_window, text="Low", command=set_low)
    low_button.pack(pady=5)
    
# add priority button
priority_button = tk.Button(root, text="Set Priority", command=set_priority)
priority_button.pack(pady=5)
priority_button.config(bg="#EDE7F6")


#delete task function
def delete_task():
    selected_task = listbox.curselection()
    if not selected_task:
        return
    listbox.delete(selected_task)

#add delete botton
delete_button=tk.Button(root, text="Delete task",command=delete_task)
delete_button.pack(pady=5)

def clear_all():
    listbox.delete(0,tk.END)

# add clear all button
clear_button=tk.Button(root, text="Clear All", command=clear_all)
clear_button.pack(pady=5)

add_button.config(bg="#EDE7F6")
delete_button.config(bg="#EDE7F6")
clear_button.config(bg="#EDE7F6")

root.mainloop()


