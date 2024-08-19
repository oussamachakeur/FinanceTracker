class Transaction:
    def __init__(self, description, amount, date):
        self.description = description
        self.amount = amount
        self.date = date

    def __str__(self):
        return f"{self.date}: {self.description} - {'$' if self.amount >= 0 else '-$'}{abs(self.amount):.2f}"
