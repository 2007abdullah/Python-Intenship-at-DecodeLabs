import tkinter as tk
from tkinter import messagebox


# ==========================================
# Expense Tracker - DecodeLabs Project 2
# ==========================================

expenses = []
total = 0.0


# ==========================================
# Add Expense
# ==========================================

def add_expense():
    global total

    description = description_entry.get().strip()
    amount_text = amount_entry.get().strip()

    # Validate description
    if not description:
        messagebox.showwarning(
            "Missing Description",
            "Please enter where the money was spent."
        )
        description_entry.focus()
        return

    # Validate amount
    if not amount_text:
        messagebox.showwarning(
            "Missing Amount",
            "Please enter an expense amount."
        )
        amount_entry.focus()
        return

    try:
        amount = float(amount_text)

        if amount <= 0:
            messagebox.showwarning(
                "Invalid Amount",
                "Expense must be greater than 0."
            )
            amount_entry.focus()
            return

        # ==================================
        # Accumulator Logic
        # Required by DecodeLabs
        # ==================================

        total = total + amount

        # Store description and amount
        expenses.append({
            "description": description,
            "amount": amount
        })

        update_expense_list()
        update_total()

        # Clear input fields
        description_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)

        description_entry.focus()

        status_label.config(
            text="✓ Expense added successfully!"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number.\n\n"
            "Example: 100 or 250.50"
        )
        amount_entry.focus()


# ==========================================
# Delete Selected Expense
# ==========================================

def delete_expense():
    global total

    selected = expense_listbox.curselection()

    if not selected:
        messagebox.showwarning(
            "No Selection",
            "Please select an expense to delete."
        )
        return

    index = selected[0]

    expense = expenses[index]

    confirm = messagebox.askyesno(
        "Delete Expense",
        f"Are you sure you want to delete?\n\n"
        f"{expense['description']}\n"
        f"Rs. {expense['amount']:,.2f}"
    )

    if confirm:

        # Subtract deleted amount from total
        total = total - expense["amount"]

        expenses.pop(index)

        update_expense_list()
        update_total()

        status_label.config(
            text="✓ Expense deleted successfully!"
        )


# ==========================================
# Clear All Expenses
# ==========================================

def clear_expenses():
    global total

    if not expenses:
        messagebox.showinfo(
            "No Expenses",
            "There are no expenses to clear."
        )
        return

    confirm = messagebox.askyesno(
        "Clear All Expenses",
        "Are you sure you want to delete all expenses?"
    )

    if confirm:

        expenses.clear()

        total = 0.0

        update_expense_list()
        update_total()

        status_label.config(
            text="✓ All expenses cleared."
        )


# ==========================================
# Update Expense List
# ==========================================

def update_expense_list():

    expense_listbox.delete(0, tk.END)

    for index, expense in enumerate(expenses, start=1):

        description = expense["description"]
        amount = expense["amount"]

        expense_listbox.insert(
            tk.END,
            f"  {index}.  {description}"
            f"  —  Rs. {amount:,.2f}"
        )


# ==========================================
# Update Total
# ==========================================

def update_total():

    total_label.config(
        text=f"Rs. {total:,.2f}"
    )

    count = len(expenses)

    if count == 0:
        count_label.config(
            text="0 expenses"
        )

    elif count == 1:
        count_label.config(
            text="1 expense"
        )

    else:
        count_label.config(
            text=f"{count} expenses"
        )


# ==========================================
# Exit Application
# ==========================================

def exit_application():

    if expenses:

        confirm = messagebox.askyesno(
            "Exit",
            "Are you sure you want to exit?"
        )

        if not confirm:
            return

    root.destroy()


# ==========================================
# Main Window
# ==========================================

root = tk.Tk()

root.title("Expense Tracker | DecodeLabs")
root.geometry("800x700")
root.minsize(700, 600)

root.configure(bg="#121212")


# ==========================================
# Fonts
# ==========================================

title_font = (
    "Segoe UI",
    26,
    "bold"
)

subtitle_font = (
    "Segoe UI",
    11
)

heading_font = (
    "Segoe UI",
    15,
    "bold"
)

button_font = (
    "Segoe UI",
    10,
    "bold"
)


# ==========================================
# Header
# ==========================================

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
    text="💰  EXPENSE TRACKER",
    font=title_font,
    bg="#121212",
    fg="white"
)

title_label.pack(
    anchor="w"
)


subtitle_label = tk.Label(
    header_frame,
    text="Track where your money goes and monitor your total spending.",
    font=subtitle_font,
    bg="#121212",
    fg="#999999"
)

subtitle_label.pack(
    anchor="w",
    pady=(5, 0)
)


# ==========================================
# Total Card
# ==========================================

total_frame = tk.Frame(
    root,
    bg="#1E1E1E"
)

total_frame.pack(
    fill="x",
    padx=35,
    pady=15
)


total_title = tk.Label(
    total_frame,
    text="TOTAL SPENT",
    font=("Segoe UI", 10, "bold"),
    bg="#1E1E1E",
    fg="#999999"
)

total_title.pack(
    pady=(18, 0)
)


total_label = tk.Label(
    total_frame,
    text="Rs. 0.00",
    font=("Segoe UI", 28, "bold"),
    bg="#1E1E1E",
    fg="#4CAF50"
)

total_label.pack(
    pady=(3, 5)
)


count_label = tk.Label(
    total_frame,
    text="0 expenses",
    font=("Segoe UI", 10),
    bg="#1E1E1E",
    fg="#777777"
)

count_label.pack(
    pady=(0, 18)
)


# ==========================================
# Input Section
# ==========================================

input_frame = tk.Frame(
    root,
    bg="#1E1E1E"
)

input_frame.pack(
    fill="x",
    padx=35,
    pady=10
)


# Description
description_entry = tk.Entry(
    input_frame,
    font=("Segoe UI", 11),
    bg="#2A2A2A",
    fg="white",
    insertbackground="white",
    relief="flat"
)

description_entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(15, 8),
    pady=15,
    ipady=10
)


description_entry.insert(
    0,
    ""
)


# Amount
amount_entry = tk.Entry(
    input_frame,
    font=("Segoe UI", 11),
    bg="#2A2A2A",
    fg="white",
    insertbackground="white",
    relief="flat",
    width=18
)

amount_entry.pack(
    side="left",
    padx=8,
    pady=15,
    ipady=10
)


# Add button
add_button = tk.Button(
    input_frame,
    text="+  ADD",
    font=button_font,
    bg="#4CAF50",
    fg="white",
    activebackground="#45A049",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=add_expense
)

add_button.pack(
    side="right",
    padx=(8, 15),
    pady=15,
    ipadx=10,
    ipady=9
)


# ==========================================
# Input Labels
# ==========================================

description_hint = tk.Label(
    root,
    text="Description: e.g. Groceries, Transport, Food",
    font=("Segoe UI", 9),
    bg="#121212",
    fg="#666666"
)

description_hint.pack(
    anchor="w",
    padx=50
)


amount_hint = tk.Label(
    root,
    text="Amount: e.g. 500 or 250.50",
    font=("Segoe UI", 9),
    bg="#121212",
    fg="#666666"
)

amount_hint.pack(
    anchor="w",
    padx=50
)


# ==========================================
# Enter Key
# ==========================================

amount_entry.bind(
    "<Return>",
    lambda event: add_expense()
)


description_entry.bind(
    "<Return>",
    lambda event: amount_entry.focus()
)


# ==========================================
# Expense Header
# ==========================================

expense_header = tk.Frame(
    root,
    bg="#121212"
)

expense_header.pack(
    fill="x",
    padx=35,
    pady=(20, 5)
)


expenses_title = tk.Label(
    expense_header,
    text="Expense History",
    font=heading_font,
    bg="#121212",
    fg="white"
)

expenses_title.pack(
    side="left"
)


# ==========================================
# Expense List
# ==========================================

list_frame = tk.Frame(
    root,
    bg="#1E1E1E"
)

list_frame.pack(
    fill="both",
    expand=True,
    padx=35,
    pady=10
)


scrollbar = tk.Scrollbar(
    list_frame
)

scrollbar.pack(
    side="right",
    fill="y"
)


expense_listbox = tk.Listbox(
    list_frame,
    font=("Segoe UI", 11),
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

expense_listbox.pack(
    side="left",
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


scrollbar.config(
    command=expense_listbox.yview
)


# ==========================================
# Action Buttons
# ==========================================

button_frame = tk.Frame(
    root,
    bg="#121212"
)

button_frame.pack(
    fill="x",
    padx=35,
    pady=5
)


delete_button = tk.Button(
    button_frame,
    text="🗑  Delete Selected",
    font=button_font,
    bg="#C62828",
    fg="white",
    activebackground="#B71C1C",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=delete_expense
)

delete_button.pack(
    side="left",
    ipadx=10,
    ipady=7,
    padx=(0, 8)
)


clear_button = tk.Button(
    button_frame,
    text="🧹  Clear All",
    font=button_font,
    bg="#444444",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=clear_expenses
)

clear_button.pack(
    side="left",
    ipadx=10,
    ipady=7
)


exit_button = tk.Button(
    button_frame,
    text="✕  Exit",
    font=button_font,
    bg="#252525",
    fg="#DDDDDD",
    activebackground="#333333",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=exit_application
)

exit_button.pack(
    side="right",
    ipadx=15,
    ipady=7
)


# ==========================================
# Status Bar
# ==========================================

status_label = tk.Label(
    root,
    text="Ready — Add your first expense!",
    font=("Segoe UI", 9),
    bg="#121212",
    fg="#777777"
)

status_label.pack(
    fill="x",
    padx=35,
    pady=(5, 20)
)


# ==========================================
# Start Application
# ==========================================

description_entry.focus()

root.mainloop()