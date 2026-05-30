print("Hello, Welcome To SpendWise.")
print("SpendWise is an all Expense Tracker that helps you track your spending habit.")
print("To get started, Kindly see below what i can help you with")

print("1. Log an expense")
print("2. View expense history")

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
    amount = float(input("how much did you spend? "))
    return amount

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
print(log_expense())

print("Thanks for the info provided. \nWe are keeping track")