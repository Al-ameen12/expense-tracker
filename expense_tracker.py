import json

print("Hello, Welcome To SpendWise.")
print("SpendWise is an all Expense Tracker that helps you track your spending habit.")
print("To get started, Kindly choose an option between 1 - 3")

# add date function
def add_date():
    date = input("Enter Date: ")
    return date

# add expense description
def add_desc():
    exp_desc = input("your expenses was on what? ")
    return exp_desc

# add amount
def add_amt():
    while True:
        try:
            amount = float(input("how much did you spend? "))
            if amount <= 0:
                print("Amount must be greater than zero. \nplease enter a valid amount")
            else:
                return amount
        except (ValueError):
            print("Invalid input. Please enter a number e.g.2500. Don't add amount in words nor add comma to numbers.")
    
    
# add category
def add_cat():
    category = input("in what category does your expenses fall in to?\n(e.g. Housing, Food, Utility, Transport, Black Tax)")
    return category

# add payment method
def add_p_method():
    pay_method = input("how did you pay?\n(e.g. Cash, Debit Card, Credit Card)")
    return pay_method

def log_expense ():
    expense = {}

    expense['date'] = add_date()
    expense['description'] = add_desc()
    expense['amount'] = add_amt()
    expense['category'] = add_cat()
    expense['payment_method'] = add_p_method()

    return expense

# load expenses file
def load_expenses():
    try:
        with open('spendwise.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
# save expenses to json
def save_expenses(expenses):
    with open('spendwise.json', 'w') as file:
        json.dump(expenses, file)

# view saved expenses
def view_expenses():
    expenses = load_expenses()
    for expense in expenses:
        print('---')
        print(f"Date: {expense['date']}")
        print(f"Description: {expense['description']}")
        print(f"Amount: {expense['amount']}")
        print(f"Category: {expense['category']}")
        print(f"Payment Method: {expense['payment_method']}")

def main():
    while True:
        print("\n1. Log an expense")
        print("2. View Expense history")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            expenses = load_expenses()
            new_expense = log_expense()
            expenses.append(new_expense)
            save_expenses(expenses)
            print('Expense save successfully!')
            print(load_expenses())
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
main()