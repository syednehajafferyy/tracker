# ==========================================================
# main.py
# Personal Finance Tracker (Console Version)
# ==========================================================

from helpers import (
    add_transaction,
    display_transactions,
    calculate_summary,
    delete_transaction,
    search_category
)

print("=" * 50)
print("      WELCOME TO PERSONAL FINANCE TRACKER")
print("=" * 50)
print("Track your income and expenses easily!")
print()


def show_menu():
    print("\n========== MENU ==========")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Show Summary")
    print("4. Search by Category")
    print("5. Delete Transaction")
    print("6. Exit")
    print("===========================")


running = True

while running:

    show_menu()

    choice = input("Enter your choice: ")

    match choice:

        # ------------------------------------
        # ADD TRANSACTION
        # ------------------------------------
        case "1":

            while True:

                try:
                    description = input("Description: ").strip()

                    if description == "":
                        print("Description cannot be empty.")
                        continue

                    category = input(
                        "Category (Food/Travel/Shopping/Bills/Salary/Other): "
                    ).strip()

                    if category == "":
                        print("Category cannot be empty.")
                        continue

                    amount = float(input("Amount: "))

                    if amount <= 0:
                        raise ValueError

                    t_type = input("Type (Income/Expense): ").capitalize()

                    if t_type not in ["Income", "Expense"]:
                        print("Type must be Income or Expense.")
                        continue

                    add_transaction(
                        description,
                        category,
                        amount,
                        t_type
                    )

                    print("\nTransaction Added Successfully!")

                    break

                except ValueError:
                    print("Invalid amount. Please enter a positive number.")

                except Exception as error:
                    print("Error:", error)

        # ------------------------------------
        # VIEW TRANSACTIONS
        # ------------------------------------
        case "2":

            records = display_transactions()

            if not records:
                print("\nNo transactions found.")
            else:

                print("\n========== TRANSACTIONS ==========")

                for i, item in enumerate(records, start=1):

                    print(f"\nRecord {i}")
                    print("-" * 25)
                    print("Description :", item["description"])
                    print("Category    :", item["category"])
                    print("Amount      :", item["amount"])
                    print("Type        :", item["type"])

        # ------------------------------------
        # SUMMARY
        # ------------------------------------
        case "3":

            summary = calculate_summary()

            print("\n========== SUMMARY ==========")
            print(f"Total Income  : {summary['income']}")
            print(f"Total Expense : {summary['expense']}")
            print(f"Balance       : {summary['balance']}")

            print("\nExpenses By Category")

            if len(summary["category"]) == 0:
                print("No expense records.")

            else:
                for key, value in summary["category"].items():
                    print(f"{key}: {value}")

        # ------------------------------------
        # SEARCH
        # ------------------------------------
        case "4":

            category = input("Enter category: ")

            result = search_category(category)

            if not result:
                print("No records found.")

            else:

                print()

                for item in result:

                    print("----------------------")
                    print("Description :", item["description"])
                    print("Category    :", item["category"])
                    print("Amount      :", item["amount"])
                    print("Type        :", item["type"])

        # ------------------------------------
        # DELETE
        # ------------------------------------
        case "5":

            records = display_transactions()

            if not records:
                print("Nothing to delete.")

            else:

                print()

                for i, item in enumerate(records, start=1):
                    print(
                        f"{i}. {item['description']} - "
                        f"{item['category']} - "
                        f"{item['amount']} ({item['type']})"
                    )

                try:
                    number = int(input("\nEnter record number to delete: "))

                    if delete_transaction(number - 1):
                        print("Record deleted successfully.")
                    else:
                        print("Invalid record number.")

                except ValueError:
                    print("Please enter a valid number.")

        # ------------------------------------
        # EXIT
        # ------------------------------------
        case "6":

            print("\nThank you for using Personal Finance Tracker!")
            running = False
            break

        # ------------------------------------
        # INVALID CHOICE
        # ------------------------------------
        case _:

            print("Invalid choice. Try again.")