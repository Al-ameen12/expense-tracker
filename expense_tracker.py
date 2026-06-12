import json
import datetime


CATEGORIES = ["Housing", "Utilities", "Food", "Transportation", 
              "Communication & Internet", "Black Tax", "Education", 
              "Healthcare", "Savings & Investments", "Others"]
PAYMENT_METHODS = ["Cash", "Debit Card", "Credit Card", "Bank Transfer"]

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
    while True:
        try:
            count = 0
            for option in PAYMENT_METHODS:
                count += 1
                print(f"{count}. {option}")

            pay_method = int(input("Select mode of Payment: ").strip())

            if 1 <= pay_method <= len(PAYMENT_METHODS):
                return PAYMENT_METHODS[pay_method - 1]
            else:
                print("Invalid input. choose between range (1 -4).")
        except ValueError:
            print("Invalid!! Choose from the option provided")

# log expense
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
    count = 1
    for expense in expenses:
        print('-'*20)
        print(f"Expense {count}.")
        print('-'*20)
        print(f"Date: {expense['date']}")
        print(f"Description: {expense['description']}")
        print(f"Amount: ₦{expense['amount']:,.2f}")
        print(f"Category: {expense['category']}")
        print(f"Payment Method: {expense['payment_method']}")
        count += 1

def total_amt():
    total = 0
    expenses = load_expenses()
    for amt in expenses:
       total += amt['amount'] 
    return total



# Filter by category
def filter_by_category():
    while True:
        try:
            expenses = load_expenses()

            count = 0
            for category_name in CATEGORIES:
                count += 1
                print(f"{count}. {category_name}")

            choice = int(input(f"filter by which category?\n\n\
            select from 1 to {len(CATEGORIES)}: ").strip())
            # when users selects last option
            if choice == len(CATEGORIES):
                custom = input("Enter your category: ").strip()
                filtered = [expense for expense in expenses if expense["category"] == custom]
                return custom, filtered
            elif 1 <= choice < len(CATEGORIES):
                chosen_category = CATEGORIES[choice - 1]
                filtered = [expense for expense in expenses if expense["category"] == chosen_category]
                return chosen_category, filtered
        except ValueError:
            print(f"Invalid input!! Enter number between 1 to {len(CATEGORIES)}")

# View filtered item
def view_filtered():
    chosen_category, filtered_expenses = filter_by_category()

    if not filtered_expenses:
        print(f"No expenses found for  {chosen_category}.")
        return
    print(f"--- Expenses for {chosen_category} ---")
    for expense in filtered_expenses:
        print('---')
        print(f"Date: {expense['date']}")
        print(f"Description: {expense['description']}")
        print(f"Amount: ₦{expense['amount']:,.2f}")
        print(f"Category: {expense['category']}")
        print(f"Payment Method: {expense['payment_method']}")

# Delete Expenses
def delete_expenses():
    expenses = load_expenses()

    while True:
        try:
            count = 1
            for expense in expenses:

                print('-'*20)
                print(f"Expense {count}.")
                print('-'*20)
                print(f"Date: {expense['date']}")
                print(f"Description: {expense['description']}")
                print(f"Amount: ₦{expense['amount']:,.2f}")
                print(f"Category: {expense['category']}")
                print(f"Payment Method: {expense['payment_method']}")

                count += 1

            delete_item = int(input("Enter the Expense to be deleted: ").strip())

            if 1 <= delete_item <= len(expenses):
                deleted_expense = expenses.pop(delete_item -1)
                save_expenses(expenses)
                return f"Success! \'{deleted_expense['description']}\' expense has been deleted."
            else:
                return "Error! Invalid Selection number"
        except ValueError:
            print("\nError encountered. Wrong Value Input. Pls try again\n")


def main():   
        print("Hello, Welcome To SpendWise.")
        print("SpendWise is an all Expense Tracker that helps you track your spending habit.")
        print("To get started, Kindly choose an option between 1 - 3")

        while True:
            print("\n1. Log an expense")
            print("2. View Logged Expense or Expense history")
            print("3. View Total Spending")
            print("4. Filter Expenses by Category")
            print("5. Delete an Expense")
            print("6. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                expenses = load_expenses()
                new_expense = log_expense()
                expenses.append(new_expense)
                save_expenses(expenses)
                print('************\nExpense save successfully!\n************')
            elif choice == "2":
                print("************\nHere are what you have spent your money on\n************")
                view_expenses()
            elif choice == "3":
                print(f"************\nTotal Spending: ₦{total_amt():,.2f}\n************")
            elif choice == "4":
                view_filtered()
            elif choice == "5":
                print("************\nDelete Expenses\n************")
                result = delete_expenses()
                print(result)
            elif choice == "6":
                print("************\nGoodbye!\n************")
                break
            else:
                print("Invalid choice. Try again.")
main()