import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self, data_file='expenses.json'):
        self.data_file = data_file
        self.categories = {"income": {}, "expenses": {}, "savings": {}, "investments": {}}
        self.load_data()

    def load_data(self):
        """Load existing data from the JSON file."""
        try:
            with open(self.data_file, 'r') as file:
                self.categories = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No previous data found. Starting fresh.")

    def save_data(self):
        """Save the current data to the JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.categories, file, indent=4)

    def add_category(self, category_type, category_name):
        """Add a new category under income, expenses, savings, or investments."""
        if category_name not in self.categories[category_type]:
            self.categories[category_type][category_name] = []
            print(f"Category '{category_name}' added to {category_type}.")
        else:
            print(f"Category '{category_name}' already exists in {category_type}.")

    def add_transaction(self, category_type, category_name, amount, date=None):
        """Add a transaction to a specific category."""
        if category_name not in self.categories[category_type]:
            print(f"Category '{category_name}' not found.")
            return
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        transaction = {"amount": amount, "date": date}
        self.categories[category_type][category_name].append(transaction)
        print(f"Transaction of {amount} added to '{category_name}' under {category_type}.")

    def generate_report(self):
        """Generate a monthly report."""
        print("\n--- Expense Report ---")
        total_income = total_expenses = total_savings = total_investments = 0
        current_month = datetime.now().month

        for category_type, categories in self.categories.items():
            for category_name, transactions in categories.items():
                for transaction in transactions:
                    transaction_month = datetime.strptime(transaction['date'], "%Y-%m-%d").month
                    if transaction_month == current_month:
                        amount = transaction['amount']
                        if category_type == "income":
                            total_income += amount
                        elif category_type == "expenses":
                            total_expenses += amount
                        elif category_type == "savings":
                            total_savings += amount
                        elif category_type == "investments":
                            total_investments += amount

        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Total Savings: ${total_savings:.2f}")
        print(f"Total Investments: ${total_investments:.2f}")

    def set_budget(self, category_name, limit):
        """Set a budget for an expense category."""
        for category_type in ['expenses']:  # Only expenses categories have budgets
            if category_name in self.categories[category_type]:
                self.categories[category_type][category_name].append({"budget_limit": limit})
                print(f"Budget of ${limit} set for '{category_name}'.")
                return
        print(f"Category '{category_name}' not found.")

    def check_budget_alert(self):
        """Check if any category has exceeded its budget limit."""
        for category_type, categories in self.categories.items():
            for category_name, transactions in categories.items():
                total_spent = sum(t['amount'] for t in transactions if 'amount' in t)
                for t in transactions:
                    if 'budget_limit' in t and total_spent > t['budget_limit']:
                        print(f"ALERT: '{category_name}' exceeded budget. Total spent: ${total_spent:.2f}, Budget limit: ${t['budget_limit']:.2f}")


def main():
    print("Welcome to the Expense Tracker!")
    tracker = ExpenseTracker()

    while True:
        print("\nSelect an option:")
        print("1. Add Income Category")
        print("2. Add Expense Category")
        print("3. Add Savings Category")
        print("4. Add Investment Category")
        print("5. Add Transaction")
        print("6. View Monthly Report")
        print("7. Set Budget for Expenses")
        print("8. Check Budget Alerts")
        print("9. Exit")

        choice = input("Enter choice (1-9): ").strip()

        if choice == "1":
            category_name = input("Enter Income Category Name: ").strip()
            tracker.add_category('income', category_name)

        elif choice == "2":
            category_name = input("Enter Expense Category Name: ").strip()
            tracker.add_category('expenses', category_name)

        elif choice == "3":
            category_name = input("Enter Savings Category Name: ").strip()
            tracker.add_category('savings', category_name)

        elif choice == "4":
            category_name = input("Enter Investment Category Name: ").strip()
            tracker.add_category('investments', category_name)

        elif choice == "5":
            category_type = input("Enter category type (income/expenses/savings/investments): ").strip()
            category_name = input(f"Enter {category_type} Category Name: ").strip()
            amount = float(input("Enter amount: ").strip())
            tracker.add_transaction(category_type, category_name, amount)

        elif choice == "6":
            tracker.generate_report()

        elif choice == "7":
            category_name = input("Enter Expense Category to set budget: ").strip()
            limit = float(input("Enter budget limit: ").strip())
            tracker.set_budget(category_name, limit)

        elif choice == "8":
            tracker.check_budget_alert()

        elif choice == "9":
            tracker.save_data()
            print("Data saved. Exiting.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
