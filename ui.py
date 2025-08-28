import tkinter as tk 
from functools import partial
from tkinter import messagebox
import commands

def handle_update(id, title, app):
    if not title:
        messagebox.showerror(
            title="Edit task", 
            message="cannot update with empty task!", 
            parent=app)
    else: 
        commands.update_tasks(id, {"title" : title})
        show_all_tasks_frame(app)



def handle_delete(id,app):
    commands.delete_task(id)
    app.update()

def submit_task(title, app): 
    if not title: 
        messagebox.showerror(
            title="Add task", 
            message="cannot add empty task", 
            parent =app)
    else:
        commands.save_task({"title": title})
    show_all_tasks_frame(app)


def show_edit_task_frame(task, app):
    frame = tk.Button(master=app)
    frame.grid(row=0, column=0, sticky="nsew",padx=10, pady=10)
    label = tk.Label(master=frame, text=f"edit task: {task["title"]}")
    label.grid()

    frame.tkraise
    #add an entry widget and show the task title
    entry= tk.Entry(master=frame)
    entry.insert(0, task["title"])
    entry.grid(column=1)
    # add a button text update for saving the changes
    update_btn = tk.Button(master=frame, text="update",
                            command=lambda: handle_update(task["_id"],
                            entry.get(), app))
    update_btn.grid(column=2, row=3)
    # add a button with with back or cancel for it to remove the frame
    cancel_btn = tk.Button(
        master=frame, 
        text="Back", 
        command=partial 
        (show_all_tasks_frame,app))
    cancel_btn.grid(column=3, row=2)

    frame.tkraise()
 

def show_add_tasks_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew",padx=10, pady=10)

    label = tk.Label(master=frame, text="what do you want to do?")
    label.grid()
    entry= tk.Entry(master=frame)
    entry.grid()
    btn = tk.Button(
        master=frame, 
        text="Submit",
        command=lambda:submit_task(entry.get(), app))
    btn.grid()


    frame.tkraise()

def show_all_tasks_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0,column=0, sticky="nsew", padx=10, pady=10)
               
    tasks = commands.get_tasks().to_list()
    for task in tasks:
        checkbtn = tk.Checkbutton(master = frame, text=task["title"])
        checkbtn.grid(row=tasks.index(task), column=8)

        btn=tk.Button(
            master=frame, text="Delete", 
            command=partial(handle_delete,task["_id"],app))
        btn.grid(row=tasks.index(task), column=1)

        edit_btn = tk.Button(
            master=frame, text="edit", 
            command=partial(show_edit_task_frame,task, app))
        edit_btn.grid(row=tasks.index(task), column= 2)

    btn = tk.Button(master=frame, text="Add Task", command=lambda:show_add_tasks_frame(app))
    btn.grid(row=len(tasks) + 1, column=1)

    frame.tkraise()