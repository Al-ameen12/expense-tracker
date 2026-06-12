# unit testing

pool = [{"date": "20th May, 2026", "description": "Groceries", "amount": 20000.0, "category": "Housing", "payment_method": "Cash"}, {"date": "30th May, 2026", "description": "Groceries", "amount": 40000.0, "category": "Food", "payment_method": "Cash"}, {"date": "29th May, 2026", "description": "Veggies", "amount": 60000.0, "category": "Food", "payment_method": "Cash"}, {"date": "28th May, 2026", "description": "I bought a running boot", "amount": 70000.0, "category": "Fitness", "payment_method": "Debit Card"}, {"date": "2 May, 2026", "description": "I travelled to England", "amount": 30000000.0, "category": "Transport", "payment_method": "Debit Card"}, {"date": "3 May, 2026", "description": "I book a game on sporty bet", "amount": 500.0, "category": "Betting", "payment_method": "Debit Card"}, {"date": "wrong date", "description": "i can't remember", "amount": 300.0, "category": "may be black tax", "payment_method": "crypto"}, {"date": "20/04/2091", "description": "I bought Fast food", "amount": 1000.0, "category": "Food", "payment_method": "Cash"}, {"date": "1", "description": "Bus fare", "amount": 5000.0, "category": "Transport", "payment_method": "Cash"}, {"date": "1", "description": "Bus fare", "amount": 5000.0, "category": "Transport", "payment_method": "Cash"}, {"date": "1", "description": "Bus fare", "amount": 5000.0, "category": "Transport", "payment_method": "Cash"}, {"date": "02/06/2026", "description": "Bus fare", "amount": 5000.0, "category": "Transport", "payment_method": "Cash"}, {"date": "03/06/2026", "description": "I got battery from the store", "amount": 3000.0, "category": "Utilities", "payment_method": "Credit Card"}, {"date": "03/06/2026", "description": "I paid rent", "amount": 700000.0, "category": "Housing", "payment_method": "Debit Card"}, {"date": "08/06/2026", "description": "I bought noodles", "amount": 50000.0, "category": "Food", "payment_method": "Debit Card"}]

CATEGORIES = ["Housing", "Utilities", "Food", "Transportation", 
              "Communication & Internet", "Black Tax", "Education", 
              "Healthcare", "Savings & Investments", "Others"]

def delete_expenses():
    while True:
        try:

            count = 1
            for expense in pool:

                print('-'*20)
                print(f"Expense {count}.")
                print('-'*20)
                print(f"Date: {expense['date']}")
                print(f"Description: {expense['description']}")
                print(f"Amount: ₦{expense['amount']:,.2f}")
                print(f"Category: {expense['category']}")
                print(f"Payment Method: {expense['payment_method']}")

                count += 1
            delete_item = int(input("Enter the item to be deleted: ").strip())

            if 1 <= delete_item <= len(pool):
                deleted_expense = pool.pop(delete_item -1)
                return f"Success! {deleted_expense['description']} expense has been deleted."
            else:
                return "Error! Invalid Selection number"
        except:
            print("Error encountered.")
print(delete_expenses())


# def delete_expenses():
#     count = 1
#     for expense in pool:
#         print('-'*20)
#         print(f"Expense {count}.")
#         print('-'*20)
#         print(f"Date: {expense['date']}")
#         print(f"Description: {expense['description']}")
#         print(f"Amount: ₦{expense['amount']:,.2f}")
#         print(f"Category: {expense['category']}")
#         print(f"Payment Method: {expense['payment_method']}")
#         count += 1
        
#     delete_item = int(input("Enter the item to be deleted: ").strip())

#     # Check if user input matches a displayed number (1 to 15)
#     if 1 <= delete_item <= len(pool):
#         # Shift back by 1 to target correct Python index (e.g., input 15 becomes index 14)
#         deleted_expense = pool.pop(delete_item - 1)
#         return f"Success: {deleted_expense['description']} has been deleted."
#     else:
#         return "Error: Invalid selection number."

# print(delete_expenses())
# # To verify it worked, print the pool length afterwards
# print(f"Remaining items in pool: {len(pool)}")

