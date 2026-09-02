import tkinter as tk
from tkinter import messagebox


# =========================
# Task Data
# =========================

tasks = []


# =========================
# Functions
# =========================

def add_task(event=None):
    """Add a new task to the task list."""

    task = task_entry.get().strip()

    if not task:
        messagebox.showwarning(
            "Empty Task",
            "Please enter a task before adding."
        )
        task_entry.focus()
        return

    tasks.append(task)

    task_entry.delete(0, tk.END)

    update_task_list()
    update_task_count()

    status_label.config(
        text="✓ Task added successfully!"
    )

    task_entry.focus()


def delete_task():
    """Delete the selected task."""

    selected = task_listbox.curselection()

    if not selected:
        messagebox.showwarning(
            "No Selection",
            "Please select a task to delete."
        )
        return

    index = selected[0]

    confirm = messagebox.askyesno(
        "Delete Task",
        f"Are you sure you want to delete:\n\n{tasks[index]}"
    )

    if confirm:
        deleted_task = tasks.pop(index)

        update_task_list()
        update_task_count()

        status_label.config(
            text=f"✓ '{deleted_task}' deleted."
        )


def clear_tasks():
    """Remove all tasks."""

    if not tasks:
        messagebox.showinfo(
            "No Tasks",
            "There are no tasks to clear."
        )
        return

    confirm = messagebox.askyesno(
        "Clear All Tasks",
        "Are you sure you want to delete all tasks?"
    )

    if confirm:
        tasks.clear()

        update_task_list()
        update_task_count()

        status_label.config(
            text="✓ All tasks cleared."
        )


def update_task_list():
    """Refresh the task list displayed in the GUI."""

    task_listbox.delete(0, tk.END)

    for index, task in enumerate(tasks, start=1):
        task_listbox.insert(
            tk.END,
            f"  {index}. {task}"
        )


def update_task_count():
    """Update the task counter."""

    count = len(tasks)

    if count == 0:
        task_count_label.config(
            text="0 Tasks"
        )
    elif count == 1:
        task_count_label.config(
            text="1 Task"
        )
    else:
        task_count_label.config(
            text=f"{count} Tasks"
        )


def exit_app():
    """Close the application."""

    if tasks:
        confirm = messagebox.askyesno(
            "Exit",
            "Are you sure you want to exit?"
        )

        if not confirm:
            return

    root.destroy()


# =========================
# Main Window
# =========================

root = tk.Tk()

root.title("To-Do List | DecodeLabs")
root.geometry("750x650")
root.minsize(650, 550)

root.configure(bg="#121212")


# =========================
# Fonts
# =========================

TITLE_FONT = ("Segoe UI", 26, "bold")
SUBTITLE_FONT = ("Segoe UI", 11)
HEADING_FONT = ("Segoe UI", 15, "bold")
NORMAL_FONT = ("Segoe UI", 11)
BUTTON_FONT = ("Segoe UI", 10, "bold")


# =========================
# Header
# =========================

header_frame = tk.Frame(
    root,
    bg="#121212"
)

header_frame.pack(
    fill="x",
    padx=35,
    pady=(30, 10)
)


title_label = tk.Label(
    header_frame,
    text="✓  TO-DO LIST",
    font=TITLE_FONT,
    bg="#121212",
    fg="white"
)

title_label.pack(anchor="w")


subtitle_label = tk.Label(
    header_frame,
    text="Organize your tasks. Stay productive.",
    font=SUBTITLE_FONT,
    bg="#121212",
    fg="#999999"
)

subtitle_label.pack(
    anchor="w",
    pady=(5, 0)
)


# =========================
# Add Task Section
# =========================

input_frame = tk.Frame(
    root,
    bg="#1E1E1E"
)

input_frame.pack(
    fill="x",
    padx=35,
    pady=20
)


task_entry = tk.Entry(
    input_frame,
    font=("Segoe UI", 12),
    bg="#2A2A2A",
    fg="white",
    insertbackground="white",
    relief="flat"
)

task_entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(15, 10),
    pady=15,
    ipady=8
)

task_entry.insert(
    0,
    ""
)


add_button = tk.Button(
    input_frame,
    text="+  ADD TASK",
    font=BUTTON_FONT,
    bg="#4CAF50",
    fg="white",
    activebackground="#45A049",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=add_task
)

add_button.pack(
    side="right",
    padx=(0, 15),
    pady=15,
    ipadx=10,
    ipady=8
)


# Enter key support
task_entry.bind(
    "<Return>",
    add_task
)


# =========================
# Task Header
# =========================

task_header = tk.Frame(
    root,
    bg="#121212"
)

task_header.pack(
    fill="x",
    padx=35
)


tasks_label = tk.Label(
    task_header,
    text="Your Tasks",
    font=HEADING_FONT,
    bg="#121212",
    fg="white"
)

tasks_label.pack(
    side="left"
)


task_count_label = tk.Label(
    task_header,
    text="0 Tasks",
    font=("Segoe UI", 10, "bold"),
    bg="#2A2A2A",
    fg="#AAAAAA",
    padx=12,
    pady=5
)

task_count_label.pack(
    side="right"
)


# =========================
# Task List Container
# =========================

list_frame = tk.Frame(
    root,
    bg="#1E1E1E"
)

list_frame.pack(
    fill="both",
    expand=True,
    padx=35,
    pady=15
)


# Scrollbar
scrollbar = tk.Scrollbar(
    list_frame
)

scrollbar.pack(
    side="right",
    fill="y"
)


# Listbox
task_listbox = tk.Listbox(
    list_frame,
    font=("Segoe UI", 12),
    bg="#1E1E1E",
    fg="#E0E0E0",
    selectbackground="#4CAF50",
    selectforeground="white",
    activestyle="none",
    relief="flat",
    borderwidth=0,
    highlightthickness=0,
    yscrollcommand=scrollbar.set
)

task_listbox.pack(
    side="left",
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


scrollbar.config(
    command=task_listbox.yview
)


# =========================
# Buttons
# =========================

button_frame = tk.Frame(
    root,
    bg="#121212"
)

button_frame.pack(
    fill="x",
    padx=35,
    pady=(5, 10)
)


delete_button = tk.Button(
    button_frame,
    text="🗑  Delete Selected",
    font=BUTTON_FONT,
    bg="#C62828",
    fg="white",
    activebackground="#B71C1C",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=delete_task
)

delete_button.pack(
    side="left",
    padx=(0, 8),
    ipadx=10,
    ipady=7
)


clear_button = tk.Button(
    button_frame,
    text="🧹  Clear All",
    font=BUTTON_FONT,
    bg="#444444",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=clear_tasks
)

clear_button.pack(
    side="left",
    ipadx=10,
    ipady=7
)


exit_button = tk.Button(
    button_frame,
    text="✕  Exit",
    font=BUTTON_FONT,
    bg="#252525",
    fg="#DDDDDD",
    activebackground="#333333",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=exit_app
)

exit_button.pack(
    side="right",
    ipadx=15,
    ipady=7
)


# =========================
# Status Bar
# =========================

status_label = tk.Label(
    root,
    text="Ready — Add your first task!",
    font=("Segoe UI", 9),
    bg="#121212",
    fg="#777777"
)

status_label.pack(
    fill="x",
    padx=35,
    pady=(0, 20)
)


# =========================
# Start Application
# =========================

task_entry.focus()

root.mainloop()