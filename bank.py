class Bank:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return 'Deposit successful !!! '
        else:
            return "Balance must be grater than 0"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return 'Withdraw successful !!! '
        else:
            return 'Not Enough Balance for Withdraw ...'

    def balanceInq(self):
        return self.balance

    def __str__(self):
        return f'User Name : {self.name} and Balance : {self.balance}'


print('Welcome to Ostad Bank')
print('---------------------')
name, balance = input('Your Name & Initial Balance (comma separated): ').split(',')
balance = int(balance)
account = Bank(name, balance)
while True:
    print('1. Check Balance ')
    print('2. Withdraw Money')
    print('3. Deposit Money ')
    print('4. Exit ')
    op = int(input('Select a Option: '))
    if op == 1:
        print(f'Your Balance is {account.balanceInq()} taka')
    elif op == 2:
        amount = int(input("Withdraw Amount : "))
        if amount <= account.balanceInq():
            account.balance -= amount
            print('Withdraw Successful !!! ')
        else:
            print('Account Balance too low !!! please deposit money ')
    elif op == 3:
        amount = int(input("Deposit Amount : "))
        if amount <= 0:
            print('Enter a Positive Amount  ')
        else:
            account.balance += amount
            print('Deposit Successful')
    elif op == 4:
        print('Thanks for using our bank ')
        break
    else:
        print('Wrong input ... please correct option choose ')






