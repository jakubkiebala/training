class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
    
    def deposit(self):
        while True:
            amount = input('Enter the number: ')
            try:
                amount = float(amount)
                if amount >= 0:
                    self.balance += amount
                    break
                else:
                    print('You cannot add this number')
            except ValueError:
                print('Invalid input, try again')

    def withdraw(self):
        while True:
            amount = input('Enter the number: ')
            try:
                amount = float(amount)
                if self.balance < amount:
                    print('You dont have that money in your account')
                elif amount >= 0:
                    self.balance -= amount
                    break
                else:
                    print('you cannot add this number')
            except ValueError:
                print('Invalid input, try again')
        
    def __str__(self):
        return f'Welcome {self.owner}, your bank account is about |{self.balance}|'
