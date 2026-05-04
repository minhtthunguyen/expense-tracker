import os
from datetime import date
today = date.today()
def show_menu():
    print("--- Expense Tracker ---")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View spending by category")
    print("4. View total spending")
    print("5. Quit")
    option = input("Choose an option (1-5): ")
    return option

def add_expense(expenses):
    category = input("Enter category (Food, Transport, Entertainment, etc.): ").capitalize()
    money_amount = float(input("Enter amount: "))
    description = input("Enter description: ").capitalize()
    today = date.today()
    expense = {"category": category, "money_amount": money_amount, "date": today, "description": description}
    expenses.append(expense)
    print(f"${round(money_amount,2)} for {category} on {str(today)} ")
    return expense

def view_expense(expenses):
    print("--- All Expenses ---")
    if len(expenses) == 0:
        print("No expenses found")
    for i in range(len(expenses)):
        print(f"{i+1}. |{expenses[i]['date']} |{expenses[i]['category']} | {expenses[i]['money_amount']} | {expenses[i]['description']}")

def category_spending(expenses):
    totals = {}
    print("--- Spending by Category ---")
    for expense in expenses:
        category = expense['category']
        amount = expense['money_amount']
        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount    
    for category, amount in totals.items(): 
        print(f"{category}: ${amount}")
    return totals
    
def view_total(expenses):
        total = 0
        for expense in expenses:
            total += expense['money_amount']
        print(f"Total spending: ${total}")
              
expenses = []
while True:
    choice = show_menu()
    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        view_expense(expenses)
    elif choice == "3":
        category_spending(expenses)
    elif choice == "4":
        view_total(expenses)
    elif choice == "5":
        print("Goodbye!")
        break