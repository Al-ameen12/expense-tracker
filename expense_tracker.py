import json
import datetime


CATEGORIES = ["Housing", "Utilities", "Food", "Transportation", 
              "Communication & Internet", "Black Tax", "Education", 
              "Healthcare", "Savings & Investments", "Others"]

print("Hello, Welcome To SpendWise.")
print("SpendWise is an all Expense Tracker that helps you track your spending habit.")
print("To get started, Kindly choose an option between 1 - 3")

# add date function
def add_date():
    while True:
        date = input("Enter Date (DD/MM/YYYY) or press 1 for Today's Date: ").strip()
        if date == "1":            
            return datetime.datetime.today().strftime("%d/%m/%Y")
        try:
            datetime.datetime.strptime(date, "%d/%m/%Y")
            return date
        except ValueError:
            print("Invalid format. Use DD/MM/YYYY e.g. 02/06/2026.")

# add expense description 
def add_desc():
    while True:
        exp_desc = input("What was the expense for? ").strip()
        if exp_desc == "":
            print("Description cannot be empty!!\n" \
                "e.g. Bought Amala from Yakoyo")
        elif len(exp_desc) < 3:
            print("Description is too short!! Please provide a bit more detail.\n" \
            "e.g. Bus fare.")
        elif exp_desc.replace('.', '', 1).isdigit():
            print('Description cannot be just numbers!! Please describe the expense.\n' \
            'e.g. Bought amala from Yakoyo')
        else:
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
    while True:
        try:
            print("Your Expenses is in what category? ")
            count = 0
            for option in CATEGORIES:
                count += 1
                print(f"{count}. {option}")

            category = int(input("Choose from the CATEGORIES above: ").strip())

            # when users selects last option
            if category == len(CATEGORIES):
                category = input("Enter your category: ").strip()
                return category
            elif 1 <= category < len(CATEGORIES):
                return CATEGORIES[category - 1]
            else:
                print("Wrong input. Please choose a number from the list.")  
        except ValueError:
            print("Wrong input, try again.")

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