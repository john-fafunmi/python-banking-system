import datetime

class User:
    def __init__(self, name):
        self.name = name
        self.account = Account(self.name)
class Account:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.balance = 0
        self.transactions = []
        self.is_active = True
        self.secret_code = owner_name.strip().lower()

    def deposit(self, amount):
        if not self.is_active:
            print("Transaction Incomplete: Account is frozen")
            return False
        
        if amount <= 0:
            print("Deposit an amount greater than 0: ")
            return False
        
        self.balance += amount
        print(f"Successfully depositted ${amount:.2f}")
        deposit_tx = Transaction(amount, None, self.owner_name, "Deposit")
        self.transactions.append(deposit_tx)
        return True


    def withdraw(self,amount):
        if not self.is_active:
            print("Transaction Incomplete: Account is frozen")
            return False
        
        if amount > self.balance:
            print("Insufficient Funds")
            return False
        if amount <= 0:
            print("Withdrawal amount has to be atleast $0.01 ")
            return False
        self.balance -= amount
        print(f"Successfully withdrew ${amount:.2f}")
        withdrawal_tx = Transaction(amount, self.owner_name, None, "Withdrawal")
        self.transactions.append(withdrawal_tx)
        return True

    def transfer(self, amount, target_account):
        if not self.is_active:
            print("Transaction Incomplete: Account is frozen")
            return False
        
        if amount > self.balance:
            print("Insufficient Funds")
            return False
        if amount <= 0:
            print("You cant trasfer an amount less than or equal to 0! ")
            return False
        
        
        self.balance -= amount
        print(f"Successfully transferred ${amount:.2f} to {target_account.owner_name}")
        transfer_tx = Transaction(amount, self.owner_name, target_account.owner_name, "Transfer Out")
        self.transactions.append(transfer_tx)
        target_account.balance += amount
        target_account_tx = Transaction(amount, self.owner_name, target_account.owner_name, "Transfer In")
        target_account.transactions.append(target_account_tx)
        return True

    def account_freeze(self):
            self.is_active = False

    def account_unfreeze(self, authentication):
        if authentication.lower() != self.secret_code:
            print("That is not the secret code")
        else:
            print("Correct, your account is now unfrozen! ")
            self.is_active = True

    
class Transaction:
    def __init__(self, amount, sender, receiver, type_transaction):
        self.amount = amount
        self.sender = sender
        self.receiver = receiver
        self.type_transaction = type_transaction
        self.timestamp = datetime.datetime.now()
def main():

    my_user = User("John")
    friend = User("Jameer")
    print(f"Hello {my_user.name}!\nWelcome to your account!")

    while True:
        print("\n--------BANK ACCOUNT OPTIONS--------")
        print("       Type 1 to check balance")
        print("        Type 2 for deposit      ")
        print("       Type 3 for withdrawal   ")
        print("       Type 4 for transfer      ")
        print("   Type 5 to view transaction history      ")
        print("           Type 6 to exit!     ")
        number = input("Which option? (1-6): ").strip()

        if number == '1':
            print(f"{my_user.name}'s balance is currently ${my_user.account.balance:.2f}")
        elif number == '2':
            deposit = float(input("How much do you want to deposit? "))
            if my_user.account.deposit(deposit):
                print(f"Your current balance is now ${my_user.account.balance:.2f} ")

        elif number == '3':
            withdrawal = float(input("How much do you want to withdraw? "))
            if my_user.account.withdraw(withdrawal):
                print(f"Your current balance is ${my_user.account.balance:.2f} ")

        elif number == '4':
            transfer = float(input(f"How much do you want to transfer to {friend.name}? "))
            if my_user.account.transfer(transfer, friend.account):
                print(f"Your current balance is ${my_user.account.balance:.2f} ")

        elif number == '5':
            for index, transaction in enumerate(my_user.account.transactions):
                print(f"Transaction {index + 1}. ${transaction.amount:.2f} | Sender: {transaction.sender} | Receiver: {transaction.receiver} | Type: {transaction.type_transaction} | Time: {transaction.timestamp}")
                
        elif number == '6':
            print("You have successfully Exitted!")
            return
        else:
            print("Please enter a number from 1-6: ")
main()
