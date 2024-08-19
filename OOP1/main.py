from transaction import Transaction
from finance_tracker import FinanceTracker
from data_handler import save_data, load_data

def main():
    filename = "transactions.dat"
    finance_tracker = load_data(filename) or FinanceTracker()

    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Transaction")
        print("2. Remove Transaction")
        print("3. View Transactions")
        print("4. Get Balance")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            transaction = Transaction(description, amount, date)
            finance_tracker.add_transaction(transaction)

        elif choice == "2":
            finance_tracker.view_transactions()
            index = int(input("Enter the index of the transaction to remove: "))
            finance_tracker.remove_transaction(index)

        elif choice == "3":
            finance_tracker.view_transactions()

        elif choice == "4":
            balance = finance_tracker.get_balance()
            print(f"Current balance: ${balance:.2f}")

        elif choice == "5":
            save_data(finance_tracker, filename)
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
