# PROJECT 3
# PYTHON PROGRAMMING INTERNSHIP - MOTION CUT
# AUTHOR: KARAN DIUNDI

# Expense Tracker Application

import datetime

# Data structure to store expenses
expenses = []

# Function to input a new expense
def add_expense():
    try:
        amount = float(input("Enter the amount spent: "))  # Taking input for amount
        description = input("Enter a brief description of the expense: ")  # Description
        category = input("Enter the category (e.g., Food, Transport, Entertainment): ").capitalize()  # Categorization
        date = datetime.datetime.now().strftime("%Y-%m-%d")  # Automatically adding today's date

        expense = {
            'amount': amount,
            'description': description,
            'category': category,
            'date': date
        }

        expenses.append(expense)  # Storing expense data
        print("Expense added successfully!")

    except ValueError:
        print("Invalid input! Please enter a numeric value for amount.")

# Function to display expenses
def display_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense['date']} - {expense['description']}: Rs.{expense['amount']} (Category: {expense['category']})")

# Function to view expense summary by month
def monthly_summary():
    month = input("Enter the month (YYYY-MM): ")
    total_spent = 0
    for expense in expenses:
        if expense['date'].startswith(month):
            total_spent += expense['amount']
    print(f"Total expenses for {month}: Rs.{total_spent:.2f}")

# Function to display expenses by category
def category_summary():
    category = input("Enter the category: ").capitalize()
    total_spent = 0
    for expense in expenses:
        if expense['category'] == category:
            total_spent += expense['amount']
    print(f"Total spent on {category}: Rs.{total_spent:.2f}")

# Main menu function
def menu():
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Monthly Summary")
        print("4. View Category Summary")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            display_expenses()
        elif choice == '3':
            monthly_summary()
        elif choice == '4':
            category_summary()
        elif choice == '5':
            print("Exiting Expense Tracker. Have a great day!")
            break
        else:
            print("Invalid option! Please choose a valid menu option.")

# Running the program
menu()
