class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
        self.pin = None

    def pin_set_up(self):
        pin = []
        for i in range (0, 4):
            while True:
                pin_number = input(f'Enter {i+1} number of your new pin code: ')
                if pin_number in '0123456789':
                    pin_number = int(pin_number)
                    pin.append(pin_number)
                    break
                else:
                    print(f'Incorrect data, try again {pin_number}')
        self.pin = int(''.join(str(digit) for digit in pin))


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
        return f'Welcome {self.owner}, your bank account is about |{self.balance}|, your pin : {self.pin}'
    

account = BankAccount('Kubus')
account.pin_set_up()
print(account)