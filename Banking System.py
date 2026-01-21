print("Banking System")


class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.history = []

    def deposit(self, amt):
        self.balance += amt
        self.history.append(f"Deposit {amt}")

    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amt
            self.history.append(f"Withdraw {amt}")

acc = Bank("Oishi", 1000)

acc.deposit(500)
acc.withdraw(300)

print("Balance:", acc.balance)
print("History:", acc.history)
