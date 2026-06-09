# unit testing

pool = [{"date": "20th May, 2026", "description": "Groceries", "amount": 20000.0, "category": "Housing", "payment_method": "Cash"}, {"date": "30th May, 2026", "description": "Groceries", "amount": 40000.0, "category": "Food", "payment_method": "Cash"}, {"date": "29th May, 2026", "description": "Veggies", "amount": 60000.0, "category": "Food", "payment_method": "Cash"}, {"date": "28th May, 2026", "description": "I bought a running boot", "amount": 70000.0, "category": "Fitness", "payment_method": "Debit Card"}, {"date": "2 May, 2026", "description": "I travelled to England", "amount": 30000000.0, "category": "Transport", "payment_method": "Debit Card"}, {"date": "3 May, 2026", "description": "I book a game on sporty bet", "amount": 500.0, "category": "Betting", "payment_method": "Debit Card"}, {"date": "wrong date", "description": "i can't remember", "amount": 300.0, "category": "may be black tax", "payment_method": "crypto"}, {"date": "20/04/2091", "description": "I bought Fast food", "amount": 1000.0, "category": "Food", "payment_method": "Cash"}, {"date": "1", "description": "Bus fare", "amount": 5000.0, "category": "Transport", "payment_method": "Cash"}, {"date": "1", "description": "Bus fare", "amount": 5000.0, "category": "Transport", "payment_method": "Cash"}, {"date": "1", "description": "Bus fare", "amount": 5000.0, "category": "Transport", "payment_method": "Cash"}, {"date": "02/06/2026", "description": "Bus fare", "amount": 5000.0, "category": "Transport", "payment_method": "Cash"}, {"date": "03/06/2026", "description": "I got battery from the store", "amount": 3000.0, "category": "Utilities", "payment_method": "Credit Card"}, {"date": "03/06/2026", "description": "I paid rent", "amount": 700000.0, "category": "Housing", "payment_method": "Debit Card"}, {"date": "08/06/2026", "description": "I bought noodles", "amount": 50000.0, "category": "Food", "payment_method": "Debit Card"}]

CATEGORIES = ["Housing", "Utilities", "Food", "Transportation", 
              "Communication & Internet", "Black Tax", "Education", 
              "Healthcare", "Savings & Investments", "Others"]


def filter_by_category():
    count = 0
    for category_name in CATEGORIES:
        count += 1
        print(f"{count}. {category_name}")

    choice = int(input(f"filter by which category?\n\n\
    select from 1 to {len(CATEGORIES)}: ").strip())
     # when users selects last option
    if choice == len(CATEGORIES):
        choice = input("Enter your category: ").strip()
        return "cannot extract data for now."
    elif 1 <= choice < len(CATEGORIES):
        chosen_category = CATEGORIES[choice - 1]
        filtered = [expense for expense in pool if expense["category"] == chosen_category]
        return filtered

# print(filter_by_category())
def view_filtered():
    filtered_expenses = filter_by_category()
    for expense in filtered_expenses:
        print('---')
        print(f"Date: {expense['date']}")
        print(f"Description: {expense['description']}")
        print(f"Amount: ₦{expense['amount']:,.2f}")
        print(f"Category: {expense['category']}")
        print(f"Payment Method: {expense['payment_method']}")

print(view_filtered())
