expenses = {
    "Food": 500,
    "Travel": 300,
    "Shopping": 1200,
    "Recharge": 250
}

total = sum(expenses.values())

print("Total Expense:", total)

print("\nCategory-wise Expenses:")

for category, amount in expenses.items():
    print(category, ":", amount)
