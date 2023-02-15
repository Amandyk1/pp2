class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        money = float(input())
        self.balance += money
        return Bank(self.owner, self.balance)

    def withdraw(self):
        withdrawal = float(input())
        while withdrawal > self.balance:
            withdrawal = float(input())
        self.balance -= withdrawal
        return Bank(self.owner, self.balance)

    def __str__(self):
        return {self.owner}, {self.balance}


acc = Bank(input(), float(input()))
acc = Bank.deposit(acc)
acc = Bank.withdraw(acc)
print(acc)