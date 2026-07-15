# ==========================================================
# helpers.py
# Personal Finance Tracker
# Contains all helper functions used by the CLI and GUI
# ==========================================================

import json
import os

# -----------------------------
# Global List
# -----------------------------
transactions = []

DATA_FILE = "data.json"


# -----------------------------
# Load Data
# -----------------------------
def load_data():
    global transactions

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                transactions = json.load(file)
        except:
            transactions = []
    else:
        transactions = []


# -----------------------------
# Save Data
# -----------------------------
def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(transactions, file, indent=4)


# -----------------------------
# Add Transaction
# -----------------------------
def add_transaction(description, category, amount, t_type):

    if len(description.strip()) < 3:
        raise ValueError("Description must contain at least 3 characters.")

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    transaction = {
        "description": description.capitalize(),
        "category": category.capitalize(),
        "amount": amount,
        "type": t_type.capitalize()
    }

    transactions.append(transaction)

    save_data()


# -----------------------------
# Display Transactions
# -----------------------------
def display_transactions():

    if not transactions:
        return []

    return transactions


# -----------------------------
# Delete Transaction
# -----------------------------
def delete_transaction(index):

    if index >= 0 and index < len(transactions):
        transactions.pop(index)
        save_data()
        return True

    return False


# -----------------------------
# Recursive Income
# -----------------------------
def recursive_income(index=0):

    if index == len(transactions):
        return 0

    current = transactions[index]

    if current["type"] == "Income":
        return current["amount"] + recursive_income(index + 1)

    return recursive_income(index + 1)


# -----------------------------
# Recursive Expense
# -----------------------------
def recursive_expense(index=0):

    if index == len(transactions):
        return 0

    current = transactions[index]

    if current["type"] == "Expense":
        return current["amount"] + recursive_expense(index + 1)

    return recursive_expense(index + 1)


# -----------------------------
# Category Summary
# -----------------------------
def category_summary():

    summary = {}

    for item in transactions:

        if item["type"] == "Expense":

            category = item["category"]

            if category in summary:
                summary[category] += item["amount"]
            else:
                summary[category] = item["amount"]

    return summary


# -----------------------------
# Calculate Summary
# -----------------------------
def calculate_summary():

    income = recursive_income()

    expense = recursive_expense()

    balance = income - expense

    return {
        "income": income,
        "expense": expense,
        "balance": balance,
        "category": category_summary()
    }


# -----------------------------
# Search by Category
# -----------------------------
def search_category(category):

    result = []

    for item in transactions:

        if item["category"].lower() == category.lower():
            result.append(item)

    return result


# -----------------------------
# Clear All Records
# -----------------------------
def clear_all():

    transactions.clear()

    save_data()


# -----------------------------
# Load data automatically
# -----------------------------
load_data()