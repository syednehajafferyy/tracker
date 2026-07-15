# ==========================================================
# gui.py
# Personal Finance Tracker - Tkinter GUI
# ==========================================================

import tkinter as tk
from tkinter import ttk, messagebox

from helpers import (
    add_transaction,
    display_transactions,
    delete_transaction,
    calculate_summary
)

# --------------------------------------------------
# Welcome Screen
# --------------------------------------------------

welcome = tk.Tk()
welcome.title("Welcome")
welcome.geometry("600x400")
welcome.configure(bg="#f8d7da")
welcome.resizable(False, False)

title = tk.Label(
    welcome,
    text="💰 Personal Finance Tracker",
    font=("Verdana", 24, "bold"),
    bg="#f8d7da",
    fg="#8B005D"
)
title.pack(pady=35)

subtitle = tk.Label(
    welcome,
    text="Welcome!\nManage your income and expenses easily.",
    font=("Verdana", 12),
    bg="#f8d7da"
)
subtitle.pack()

features = tk.Label(
    welcome,
    text=(
        "✔ Add Income & Expenses\n"
        "✔ Delete Transactions\n"
        "✔ View Balance\n"
        "✔ Category-wise Spending\n"
        "✔ Automatic Data Saving"
    ),
    font=("Verdana", 11),
    bg="#f8d7da",
    justify="left"
)
features.pack(pady=20)


def start_app():
    welcome.destroy()


start_button = tk.Button(
    welcome,
    text="Start Application",
    font=("Verdana", 12, "bold"),
    bg="#90EE90",
    width=20,
    command=start_app
)
start_button.pack(pady=20)

welcome.mainloop()

# --------------------------------------------------
# Main Window
# --------------------------------------------------

root = tk.Tk()
root.title("Personal Finance Tracker")
root.geometry("900x780")
root.configure(bg="#f8d7da")
root.resizable(False, False)

heading = tk.Label(
    root,
    text="Personal Finance Tracker",
    font=("Verdana", 22, "bold"),
    bg="#f8d7da",
    fg="#8B005D"
)
heading.pack(pady=15)

# --------------------------------------------------
# Input Frame
# --------------------------------------------------

frame = tk.Frame(root, bg="#f8d7da")
frame.pack(pady=10)

tk.Label(
    frame,
    text="Description",
    font=("Verdana", 10),
    bg="#f8d7da"
).grid(row=0, column=0, padx=10, pady=8)

description_entry = tk.Entry(
    frame,
    width=30,
    font=("Verdana", 10)
)
description_entry.grid(row=0, column=1)

tk.Label(
    frame,
    text="Category",
    font=("Verdana", 10),
    bg="#f8d7da"
).grid(row=1, column=0, padx=10, pady=8)

category_box = ttk.Combobox(
    frame,
    values=[
        "Food",
        "Travel",
        "Shopping",
        "Bills",
        "Salary",
        "Entertainment",
        "Education",
        "Health",
        "Other"
    ],
    state="readonly",
    width=27
)
category_box.grid(row=1, column=1)
category_box.current(0)

tk.Label(
    frame,
    text="Amount",
    font=("Verdana", 10),
    bg="#f8d7da"
).grid(row=2, column=0, padx=10, pady=8)

amount_entry = tk.Entry(
    frame,
    width=30,
    font=("Verdana", 10)
)
amount_entry.grid(row=2, column=1)

tk.Label(
    frame,
    text="Type",
    font=("Verdana", 10),
    bg="#f8d7da"
).grid(row=3, column=0, padx=10, pady=8)

type_box = ttk.Combobox(
    frame,
    values=[
        "Income",
        "Expense"
    ],
    state="readonly",
    width=27
)
type_box.grid(row=3, column=1)
type_box.current(0)
# --------------------------------------------------
# Transaction List
# --------------------------------------------------

list_title = tk.Label(
    root,
    text="Transaction History",
    font=("Verdana", 14, "bold"),
    bg="#f8d7da",
    fg="#8B005D"
)
list_title.pack(pady=(15, 5))

listbox_frame = tk.Frame(root)
listbox_frame.pack()

scrollbar = tk.Scrollbar(listbox_frame)

listbox = tk.Listbox(
    listbox_frame,
    width=100,
    height=12,
    font=("Verdana", 10),
    yscrollcommand=scrollbar.set
)

scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.pack(side=tk.LEFT)

# --------------------------------------------------
# Summary Section
# --------------------------------------------------

summary_frame = tk.Frame(root, bg="#f8d7da")
summary_frame.pack(pady=15)

income_label = tk.Label(
    summary_frame,
    text="Total Income: Rs. 0",
    font=("Verdana", 11, "bold"),
    bg="#f8d7da",
    fg="green"
)
income_label.grid(row=0, column=0, padx=20)

expense_label = tk.Label(
    summary_frame,
    text="Total Expense: Rs. 0",
    font=("Verdana", 11, "bold"),
    bg="#f8d7da",
    fg="red"
)
expense_label.grid(row=0, column=1, padx=20)

balance_label = tk.Label(
    summary_frame,
    text="Balance: Rs. 0",
    font=("Verdana", 11, "bold"),
    bg="#f8d7da",
    fg="blue"
)
balance_label.grid(row=0, column=2, padx=20)

# --------------------------------------------------
# Category-wise Spending
# --------------------------------------------------

category_title = tk.Label(
    root,
    text="Category-wise Spending",
    font=("Verdana", 14, "bold"),
    bg="#f8d7da",
    fg="#8B005D"
)
category_title.pack(pady=(10, 5))

category_box_frame = tk.Frame(root, bg="#f8d7da")
category_box_frame.pack()

category_text = tk.Text(
    category_box_frame,
    width=45,
    height=8,
    font=("Consolas", 10),
    state="disabled"
)

category_text.pack()

# --------------------------------------------------
# Buttons Frame
# --------------------------------------------------

button_frame = tk.Frame(root, bg="#f8d7da")
button_frame.pack(pady=15)
# --------------------------------------------------
# Refresh Data
# --------------------------------------------------

def refresh():

    # Clear transaction list
    listbox.delete(0, tk.END)

    records = display_transactions()

    # Display all transactions
    for i, item in enumerate(records, start=1):

        listbox.insert(
            tk.END,
            f"{i}. "
            f"{item['description']} | "
            f"{item['category']} | "
            f"Rs. {item['amount']} | "
            f"{item['type']}"
        )

    # Get summary
    summary = calculate_summary()

    income_label.config(
        text=f"Total Income: Rs. {summary['income']}"
    )

    expense_label.config(
        text=f"Total Expense: Rs. {summary['expense']}"
    )

    balance_label.config(
        text=f"Balance: Rs. {summary['balance']}"
    )

    # -----------------------------
    # Category-wise Spending
    # -----------------------------

    category_text.config(state="normal")
    category_text.delete("1.0", tk.END)

    if len(summary["category"]) == 0:

        category_text.insert(
            tk.END,
            "No expense records available."
        )

    else:

        for category, amount in summary["category"].items():

            category_text.insert(
                tk.END,
                f"{category:<15} Rs. {amount}\n"
            )

    category_text.config(state="disabled")


# --------------------------------------------------
# Add Transaction
# --------------------------------------------------

def add():

    try:

        description = description_entry.get().strip()

        category = category_box.get()

        amount = float(amount_entry.get())

        transaction_type = type_box.get()

        add_transaction(
            description,
            category,
            amount,
            transaction_type
        )

        description_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)

        category_box.current(0)
        type_box.current(0)

        refresh()

        messagebox.showinfo(
            "Success",
            "Transaction Added Successfully!"
        )

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid positive amount."
        )

    except Exception as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


# --------------------------------------------------
# Delete Transaction
# --------------------------------------------------

def delete():

    try:

        selected = listbox.curselection()

        if not selected:

            messagebox.showwarning(
                "Warning",
                "Please select a transaction first."
            )

            return

        index = selected[0]

        if delete_transaction(index):

            refresh()

            messagebox.showinfo(
                "Deleted",
                "Transaction deleted successfully!"
            )

        else:

            messagebox.showerror(
                "Error",
                "Unable to delete transaction."
            )

    except Exception as error:

        messagebox.showerror(
            "Error",
            str(error)
        )
        # --------------------------------------------------
# Buttons
# --------------------------------------------------

add_button = tk.Button(
    button_frame,
    text="Add Transaction",
    font=("Verdana", 10, "bold"),
    bg="#90EE90",
    width=18,
    command=add
)
add_button.grid(row=0, column=0, padx=10)

delete_button = tk.Button(
    button_frame,
    text="Delete Transaction",
    font=("Verdana", 10, "bold"),
    bg="#FF9999",
    width=18,
    command=delete
)
delete_button.grid(row=0, column=1, padx=10)

refresh_button = tk.Button(
    button_frame,
    text="Refresh",
    font=("Verdana", 10, "bold"),
    bg="#87CEFA",
    width=18,
    command=refresh
)
refresh_button.grid(row=0, column=2, padx=10)

# --------------------------------------------------
# Exit Button
# --------------------------------------------------

exit_button = tk.Button(
    root,
    text="Exit",
    font=("Verdana", 10, "bold"),
    bg="#D3D3D3",
    width=20,
    command=root.destroy
)
exit_button.pack(pady=10)

# --------------------------------------------------
# Footer
# --------------------------------------------------

footer = tk.Label(
    root,
    text="Personal Finance Tracker | Python Capstone Project",
    font=("Verdana", 9),
    bg="#f8d7da",
    fg="gray"
)
footer.pack(pady=10)

# --------------------------------------------------
# Load Existing Data
# --------------------------------------------------

refresh()

# --------------------------------------------------
# Run Application
# --------------------------------------------------

root.mainloop()
