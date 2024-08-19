from transaction import Transaction

class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def remove_transaction(self, index):
        if 0 <= index < len(self.transactions):
            del self.transactions[index]

    def view_transactions(self):
        for i, transaction in enumerate(self.transactions):
            print(f"{i}. {transaction}")

    def get_balance(self):
        total = 0
        for transaction in self.transactions:
            total += transaction.amount
        return total

