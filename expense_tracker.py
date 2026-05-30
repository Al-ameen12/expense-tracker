print("Hello, Welcome To SpendWise.")
print("SpendWise is an all Expense Tracker that helps you track your spending habit.")
print("To get started, Kindly")

# add date function
def add_date(date):
    date = input("Enter Date: ")
    return date

# add expense description
def add_desc(exp_desc):
    exp_desc = input("your expenses was on what? ")
    return exp_desc

# add amount
def add_amt(amount):
    amount = input("how much did you spend? ")
    return amount

# add category
def add_cat(category):
    category = input("in what category does your expenses fall in to?\n(e.g. Housing, Food, Utility, Transport, Black Tax)")
    return category

# add payment method
def add_p_method(pay_method):
    pay_method = input("how did you pay?\n(e.g. Cash, Debit Card, Credit Card)")
    return pay_method







print(add_date('date'))
print("Thanks for the info provided. \nWe are keeping track")