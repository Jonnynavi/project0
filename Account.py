class Account():
    def __init__(self, account_number, personal_Info, balance=0):
        self.account_number = account_number
        self.personal_info = personal_Info
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
    
    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Sorry you currently only have {self.balance}. Please withdraw under ${self.balance}.")
        else:
            self.balance -= amount
            print(f"You succesfully withdrawn ${amount}. you now have ${self.balance} in the bank")

    def get_balance(self):
        print(self.balance)
    
