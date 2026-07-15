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

# -----------------------------
# Window
# -----------------------------
root = tk.Tk()
root.title("Personal Finance Tracker")
root.geometry("850x650")
root.configure(bg="#f8d7da")  # Light Pink


# -----------------------------
# Title
# -----------------------------
title = tk.Label(
    root,
    text="Personal Finance Tracker",
    font=("Arial", 22, "bold"),
    bg="#f8d7da"
)
title.pack(pady=15)


# -----------------------------
# Input Frame
# -----------------------------
frame = tk.Frame(root, bg="#f8d7da")
frame.pack()

tk.Label(frame, text="Description", bg="#f8d7da").grid(row=0, column=0, padx=10, pady=5)

description_entry = tk.Entry(frame, width=25)
description_entry.grid(row=0, column=1)

tk.Label(frame, text="Category", bg="#f8d7da").grid(row=1, column=0, padx=10, pady=5)

category_box = ttk.Combobox(
    frame,
    values=[
        "Food",
        "Travel",
        "Shopping",
        "Bills",
        "Salary",
        "Entertainment",
        "Other"
    ],
    state="readonly",
    width=22
)
category_box.grid(row=1, column=1)
category_box.current(0)

tk.Label(frame, text="Amount", bg="#f8d7da").grid(row=2, column=0, padx=10, pady=5)

amount_entry = tk.Entry(frame, width=25)
amount_entry.grid(row=2, column=1)

tk.Label(frame, text="Type", bg="#f8d7da").grid(row=3, column=0, padx=10, pady=5)

type_box = ttk.Combobox(
    frame,
    values=["Income", "Expense"],
    state="readonly",
    width=22
)
type_box.grid(row=3, column=1)
type_box.current(0)


# -----------------------------
# Listbox
# -----------------------------
listbox = tk.Listbox(root, width=90, height=15)
listbox.pack(pady=20)


# -----------------------------
# Summary Labels
# -----------------------------
income_label = tk.Label(
    root,
    text="Income: 0",
    font=("Arial", 12, "bold"),
    bg="#f8d7da"
)
income_label.pack()

expense_label = tk.Label(
    root,
    text="Expense: 0",
    font=("Arial", 12, "bold"),
    bg="#f8d7da"
)
expense_label.pack()

balance_label = tk.Label(
    root,
    text="Balance: 0",
    font=("Arial", 12, "bold"),
    bg="#f8d7da"
)
balance_label.pack()


# -----------------------------
# Refresh
# -----------------------------
def refresh():

    listbox.delete(0, tk.END)

    records = display_transactions()

    for item in records:

        listbox.insert(
            tk.END,
            f"{item['description']} | "
            f"{item['category']} | "
            f"{item['amount']} | "
            f"{item['type']}"
        )

    summary = calculate_summary()

    income_label.config(text=f"Income: {summary['income']}")
    expense_label.config(text=f"Expense: {summary['expense']}")
    balance_label.config(text=f"Balance: {summary['balance']}")


# -----------------------------
# Add Transaction
# -----------------------------
def add():

    try:

        description = description_entry.get()

        category = category_box.get()

        amount = float(amount_entry.get())

        t_type = type_box.get()

        add_transaction(
            description,
            category,
            amount,
            t_type
        )

        description_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)

        refresh()

        messagebox.showinfo(
            "Success",
            "Transaction Added Successfully!"
        )

    except ValueError:

        messagebox.showerror(
            "Error",
            "Amount must be a positive number."
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


# -----------------------------
# Delete Transaction
# -----------------------------
def delete():

    try:

        selected = listbox.curselection()[0]

        delete_transaction(selected)

        refresh()

        messagebox.showinfo(
            "Deleted",
            "Transaction Deleted Successfully!"
        )

    except:

        messagebox.showwarning(
            "Warning",
            "Please select a transaction."
        )


# -----------------------------
# Buttons
# -----------------------------
button_frame = tk.Frame(root, bg="#f8d7da")
button_frame.pack(pady=10)

add_btn = tk.Button(
    button_frame,
    text="Add Transaction",
    command=add,
    width=18,
    bg="#90EE90"
)
add_btn.grid(row=0, column=0, padx=10)

delete_btn = tk.Button(
    button_frame,
    text="Delete Transaction",
    command=delete,
    width=18,
    bg="#ff9999"
)
delete_btn.grid(row=0, column=1, padx=10)

refresh_btn = tk.Button(
    button_frame,
    text="Refresh",
    command=refresh,
    width=18,
    bg="#87CEFA"
)
refresh_btn.grid(row=0, column=2, padx=10)


# -----------------------------
# Load Existing Data
# -----------------------------
refresh()

root.mainloop()