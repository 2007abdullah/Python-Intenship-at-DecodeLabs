"""
=============================================================
VAULTKEY - Random Password Generator
DecodeLabs Python Programming Internship
Project 3
=============================================================

Author: Abdullah Hayat
Technology: Python + Tkinter

Features:
    • Modern black aesthetic
    • Random password generation
    • Uppercase / lowercase letters
    • Numbers
    • Special characters
    • Password strength indicator
    • Show / hide password
    • Copy to clipboard
    • Generate / regenerate password
    • Clear password
    • Input validation
    • Laptop-friendly responsive layout

Required Modules:
    random
    string
    tkinter
=============================================================
"""

import random
import string
import tkinter as tk


# =============================================================
# COLORS
# =============================================================

BG = "#080808"
CARD = "#141414"
INPUT_BG = "#0D0D0D"
BORDER = "#292929"

WHITE = "#FFFFFF"
GRAY = "#8C8C8C"
DARK_GRAY = "#555555"

PURPLE = "#8B5CF6"
PURPLE_HOVER = "#A78BFA"

GREEN = "#22C55E"
YELLOW = "#F59E0B"
RED = "#EF4444"


# =============================================================
# APPLICATION
# =============================================================

root = tk.Tk()

root.title("VaultKey - Random Password Generator")

# Laptop-friendly size
root.geometry("850x720")
root.minsize(700, 650)

root.configure(bg=BG)


# =============================================================
# VARIABLES
# =============================================================

length_var = tk.StringVar(value="16")
password_var = tk.StringVar()

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

password_visible = True


# =============================================================
# PASSWORD GENERATOR
# =============================================================

def create_password(length):
    """Generate a random password using selected options."""

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    special = "!@#$%^&*?"

    characters = ""

    if uppercase_var.get():
        characters += uppercase

    if lowercase_var.get():
        characters += lowercase

    if numbers_var.get():
        characters += numbers

    if special_var.get():
        characters += special

    if not characters:
        raise ValueError(
            "Select at least one character type."
        )

    password = []

    # Guarantee selected character types
    if uppercase_var.get():
        password.append(random.choice(uppercase))

    if lowercase_var.get():
        password.append(random.choice(lowercase))

    if numbers_var.get():
        password.append(random.choice(numbers))

    if special_var.get():
        password.append(random.choice(special))

    if length < len(password):
        raise ValueError(
            f"Length must be at least {len(password)}."
        )

    # Remaining characters
    for _ in range(length - len(password)):
        password.append(random.choice(characters))

    # Randomize character positions
    random.shuffle(password)

    return "".join(password)


# =============================================================
# GENERATE PASSWORD
# =============================================================

def generate_password():
    """Generate and display a password."""

    try:

        length = int(length_var.get())

        if length < 4:
            show_status(
                "Password length must be at least 4.",
                RED
            )
            return

        password = create_password(length)

        password_var.set(password)

        update_strength(password)

        show_status(
            "Password generated successfully",
            GREEN
        )

    except ValueError as error:

        show_status(
            str(error),
            RED
        )


# =============================================================
# PASSWORD STRENGTH
# =============================================================

def update_strength(password):
    """Calculate password strength."""

    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if len(password) >= 16:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in "!@#$%^&*?" for c in password):
        score += 1

    if score <= 2:

        text = "WEAK"
        color = RED
        level = 1

    elif score <= 4:

        text = "MEDIUM"
        color = YELLOW
        level = 2

    else:

        text = "STRONG"
        color = GREEN
        level = 3

    strength_label.config(
        text=f"STRENGTH  •  {text}",
        fg=color
    )

    for i, bar in enumerate(strength_bars):

        if i < level:
            bar.config(bg=color)
        else:
            bar.config(bg=BORDER)


# =============================================================
# COPY PASSWORD
# =============================================================

def copy_password():
    """Copy password to clipboard."""

    password = password_var.get()

    if not password:

        show_status(
            "Generate a password first.",
            YELLOW
        )

        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    show_status(
        "Password copied to clipboard",
        GREEN
    )


# =============================================================
# CLEAR PASSWORD
# =============================================================

def clear_password():
    """Clear password."""

    password_var.set("")

    strength_label.config(
        text="STRENGTH  •  ---",
        fg=GRAY
    )

    for bar in strength_bars:
        bar.config(bg=BORDER)

    show_status(
        "Password cleared",
        GRAY
    )


# =============================================================
# SHOW / HIDE
# =============================================================

def toggle_password():
    """Show or hide generated password."""

    global password_visible

    password_visible = not password_visible

    if password_visible:

        password_entry.config(show="")
        visibility_button.config(text="HIDE")

    else:

        password_entry.config(show="•")
        visibility_button.config(text="SHOW")


# =============================================================
# STATUS
# =============================================================

def show_status(message, color):
    """Display application status."""

    status_label.config(
        text=f"●  {message}",
        fg=color
    )


# =============================================================
# BUTTON HOVER
# =============================================================

def hover_effect(button, normal, hover):

    button.bind(
        "<Enter>",
        lambda event: button.config(bg=hover)
    )

    button.bind(
        "<Leave>",
        lambda event: button.config(bg=normal)
    )


# =============================================================
# MAIN CONTAINER
# =============================================================

main = tk.Frame(
    root,
    bg=BG
)

main.pack(
    fill="both",
    expand=True,
    padx=45,
    pady=20
)


# =============================================================
# HEADER
# =============================================================

brand = tk.Label(
    main,
    text="VAULTKEY",
    font=("Segoe UI", 10, "bold"),
    fg=PURPLE,
    bg=BG
)

brand.pack(anchor="w")


title = tk.Label(
    main,
    text="Random Password Generator",
    font=("Segoe UI", 24, "bold"),
    fg=WHITE,
    bg=BG
)

title.pack(
    anchor="w",
    pady=(3, 2)
)


subtitle = tk.Label(
    main,
    text="Create strong passwords in seconds.",
    font=("Segoe UI", 10),
    fg=GRAY,
    bg=BG
)

subtitle.pack(anchor="w")


# =============================================================
# PASSWORD CARD
# =============================================================

password_card = tk.Frame(
    main,
    bg=CARD,
    highlightbackground=BORDER,
    highlightthickness=1
)

password_card.pack(
    fill="x",
    pady=18
)


password_content = tk.Frame(
    password_card,
    bg=CARD
)

password_content.pack(
    fill="x",
    padx=22,
    pady=18
)


password_heading = tk.Label(
    password_content,
    text="YOUR PASSWORD",
    font=("Segoe UI", 8, "bold"),
    fg=GRAY,
    bg=CARD
)

password_heading.pack(anchor="w")


# =============================================================
# PASSWORD INPUT
# =============================================================

password_box = tk.Frame(
    password_content,
    bg=INPUT_BG
)

password_box.pack(
    fill="x",
    pady=(8, 12)
)


password_entry = tk.Entry(
    password_box,
    textvariable=password_var,
    font=("Consolas", 16, "bold"),
    fg=WHITE,
    bg=INPUT_BG,
    insertbackground=WHITE,
    relief="flat",
    bd=0,
    show=""
)

password_entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=15,
    pady=12
)


visibility_button = tk.Button(
    password_box,
    text="HIDE",
    font=("Segoe UI", 8, "bold"),
    fg=GRAY,
    bg=INPUT_BG,
    activeforeground=WHITE,
    activebackground=INPUT_BG,
    relief="flat",
    bd=0,
    cursor="hand2",
    command=toggle_password
)

visibility_button.pack(
    side="right",
    padx=15
)


# =============================================================
# STRENGTH
# =============================================================

strength_frame = tk.Frame(
    password_content,
    bg=CARD
)

strength_frame.pack(
    fill="x"
)


strength_label = tk.Label(
    strength_frame,
    text="STRENGTH  •  ---",
    font=("Segoe UI", 8, "bold"),
    fg=GRAY,
    bg=CARD
)

strength_label.pack(
    side="left"
)


strength_bars_frame = tk.Frame(
    strength_frame,
    bg=CARD
)

strength_bars_frame.pack(
    side="right"
)


strength_bars = []

for _ in range(3):

    bar = tk.Frame(
        strength_bars_frame,
        width=45,
        height=5,
        bg=BORDER
    )

    bar.pack(
        side="left",
        padx=2
    )

    strength_bars.append(bar)


# =============================================================
# COPY BUTTON
# =============================================================

copy_button = tk.Button(
    password_content,
    text="COPY PASSWORD",
    font=("Segoe UI", 9, "bold"),
    fg=WHITE,
    bg=PURPLE,
    activeforeground=WHITE,
    activebackground=PURPLE_HOVER,
    relief="flat",
    bd=0,
    cursor="hand2",
    command=copy_password
)

copy_button.pack(
    fill="x",
    pady=(15, 0),
    ipady=7
)

hover_effect(
    copy_button,
    PURPLE,
    PURPLE_HOVER
)


# =============================================================
# SETTINGS CARD
# =============================================================

settings_card = tk.Frame(
    main,
    bg=CARD,
    highlightbackground=BORDER,
    highlightthickness=1
)

settings_card.pack(
    fill="x",
    pady=(0, 15)
)


settings = tk.Frame(
    settings_card,
    bg=CARD
)

settings.pack(
    fill="x",
    padx=22,
    pady=15
)


settings_title = tk.Label(
    settings,
    text="PASSWORD SETTINGS",
    font=("Segoe UI", 8, "bold"),
    fg=GRAY,
    bg=CARD
)

settings_title.pack(anchor="w")


# =============================================================
# LENGTH
# =============================================================

length_frame = tk.Frame(
    settings,
    bg=CARD
)

length_frame.pack(
    fill="x",
    pady=(10, 8)
)


length_label = tk.Label(
    length_frame,
    text="Password Length",
    font=("Segoe UI", 9),
    fg=WHITE,
    bg=CARD
)

length_label.pack(side="left")


length_entry = tk.Entry(
    length_frame,
    textvariable=length_var,
    font=("Segoe UI", 9, "bold"),
    fg=WHITE,
    bg=INPUT_BG,
    insertbackground=WHITE,
    justify="center",
    relief="flat",
    bd=0,
    width=6
)

length_entry.pack(
    side="right",
    ipady=5
)


# =============================================================
# CHARACTER OPTIONS
# =============================================================

checkbox_frame = tk.Frame(
    settings,
    bg=CARD
)

checkbox_frame.pack(
    fill="x"
)


def make_checkbox(text, variable, row, column):

    checkbox = tk.Checkbutton(
        checkbox_frame,
        text=text,
        variable=variable,
        font=("Segoe UI", 9),
        fg=WHITE,
        bg=CARD,
        activeforeground=WHITE,
        activebackground=CARD,
        selectcolor=PURPLE,
        cursor="hand2",
        relief="flat",
        bd=0
    )

    checkbox.grid(
        row=row,
        column=column,
        sticky="w",
        padx=(0, 30),
        pady=3
    )


make_checkbox(
    "Uppercase",
    uppercase_var,
    0,
    0
)

make_checkbox(
    "Lowercase",
    lowercase_var,
    0,
    1
)

make_checkbox(
    "Numbers",
    numbers_var,
    1,
    0
)

make_checkbox(
    "Special Characters",
    special_var,
    1,
    1
)


# =============================================================
# ACTION BUTTONS
# =============================================================

actions = tk.Frame(
    main,
    bg=BG
)

actions.pack(
    fill="x"
)


generate_button = tk.Button(
    actions,
    text="GENERATE PASSWORD",
    font=("Segoe UI", 9, "bold"),
    fg=WHITE,
    bg=PURPLE,
    activeforeground=WHITE,
    activebackground=PURPLE_HOVER,
    relief="flat",
    bd=0,
    cursor="hand2",
    command=generate_password
)

generate_button.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=8
)


clear_button = tk.Button(
    actions,
    text="CLEAR",
    font=("Segoe UI", 9, "bold"),
    fg=WHITE,
    bg="#1C1C1C",
    activeforeground=WHITE,
    activebackground="#282828",
    relief="flat",
    bd=0,
    cursor="hand2",
    command=clear_password
)

clear_button.pack(
    side="left",
    padx=(8, 0),
    ipadx=28,
    ipady=8
)


hover_effect(
    generate_button,
    PURPLE,
    PURPLE_HOVER
)

hover_effect(
    clear_button,
    "#1C1C1C",
    "#282828"
)


# =============================================================
# STATUS
# =============================================================

status_label = tk.Label(
    main,
    text="●  Ready to generate a password",
    font=("Segoe UI", 8),
    fg=GRAY,
    bg=BG
)

status_label.pack(
    pady=(12, 4)
)


# =============================================================
# FOOTER
# =============================================================

footer = tk.Label(
    main,
    text="DecodeLabs Python Programming Internship  •  Project 3",
    font=("Segoe UI", 7),
    fg=DARK_GRAY,
    bg=BG
)

footer.pack(
    pady=(2, 0)
)


# =============================================================
# KEYBOARD SHORTCUT
# =============================================================

root.bind(
    "<Return>",
    lambda event: generate_password()
)


# =============================================================
# INITIAL PASSWORD
# =============================================================

# Generate a password automatically when the application opens
generate_password()


# =============================================================
# START APPLICATION
# =============================================================

root.mainloop()