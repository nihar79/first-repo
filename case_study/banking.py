import threading
import datetime
import pandas as pd

from banking_errors import *

#Main Banking class
class Banking:

    def __init__(self):
        self.customer_data=pd.read_csv('data.csv')

    def create_new_customer(self,name,opening_balance_deposit):
        if name.strip():
            if opening_balance_deposit>=0:
                customer = {
                    "CustomerID": len(self.customer_data)+101,
                    "Name": name,
                    "AccountBalance": opening_balance_deposit
                }
                self.customer_data.loc[len(self.customer_data)]=customer
                data_file=open("data.csv","a")
                data_file.write(f"\n{customer['CustomerID'],customer['Name'],customer['AccountBalance']}")
                data_file.close()
                return PersonalBanking(customer["CustomerID"])
            else:
                raise IllegalNameOrBalanceException("Opening balance must be greater than 0.")
        else:
            raise IllegalNameOrBalanceException("Name cannot be whitespaces.")

    def get_customer_data(self,customer_id):
        customer = self.customer_data.loc[customer_id-101]
        return customer

    def deposit(self, customer_id, balance_lock, balance, amount):
        with balance_lock:
            if amount > 0:
                balance = balance + amount
                self.update_customer_balance(customer_id,balance)
                return balance
            else:
                raise ZeroOrNegativeDepositException

    def withdraw(self, customer_id,balance_lock, balance, withdrawal_amount):
        with balance_lock:
            if withdrawal_amount <= balance:
                balance = balance - withdrawal_amount
                self.update_customer_balance(customer_id,balance)
                return balance
            else:
                raise InsufficientBalanceException

    def update_customer_balance(self,customer_id,balance):
        self.customer_data.loc[customer_id-101,2]=balance

    def transaction_history(self):
        pass

#Personal banking class - unique for each user
class PersonalBanking(Banking):

    def __init__(self, customer_id):
        super().__init__()
        global balance_lock
        balance_lock = threading.Lock()
        global transaction_history
        transaction_history = []
        try:
            self.data = super().get_customer_data(customer_id)
            self.my_data()
        except KeyError:
            raise NotACustomerException

    def my_data(self):
        self.data = self.data.to_dict()
        self.id=int(self.data["CustomerID"][1:])
        self.name=self.data["Name"]
        self.balance=self.data["AccountBalance"]
        self.balance=int(self.balance[0:len(self.balance)-1])

    def deposit(self, amount):
        try:
            self.balance = super().deposit(self.id,balance_lock,self.balance,amount)
            self.update_transaction_history("deposited",amount)
        except ZeroOrNegativeDepositException as e:
            self.update_transaction_history("A Failed Deposit",0)
            print(self.name,"====>",e.args[0])

    def withdraw(self, withdrawal_amount):
        try:
            self.balance = super().withdraw(self.id,balance_lock,self.balance,withdrawal_amount)
            self.update_transaction_history("withdrawn",withdrawal_amount)
        except InsufficientBalanceException as e:
            self.update_transaction_history("A Failed Withdrawal",0)
            print(self.name,"====>",e.args[0])

    def update_transaction_history(self,action,amount):
        update=f"{datetime.datetime.now()}: {amount} was {action}. New balance is {self.balance}"
        transaction_history.append(update)

    def get_transaction_history(self):
        for transaction in transaction_history:
            print(self.name,"====>",transaction)

    def create_new_customer(self):
        message=f"New account opened. Opening Balance {self.balance}"
        transaction_history.append(message)

##User classes
#Demonstrating an existing user
class User1(threading.Thread):
    def __init__(self):
        super().__init__()
        self.id=101
        self.bank=PersonalBanking(self.id)

    def transactions(self):
        self.bank.withdraw(1000)
        self.bank.deposit(900)
        #illegal withdrawal
        self.bank.withdraw(10000000)
        self.bank.get_transaction_history()

    def run(self):
        self.transactions()

#Demonstrating an existing user
class User2(threading.Thread):
    def __init__(self):
        super().__init__()
        self.id=102
        self.bank=PersonalBanking(self.id)

    def transactions(self):
        self.bank.withdraw(1000)
        self.bank.deposit(10000)
        #Illegal deposit
        self.bank.deposit(-100)
        self.bank.get_transaction_history()

    def run(self):
        self.transactions()

#Demonstrating an Invalid User
class User3(threading.Thread):
    def __init__(self):
        super().__init__()
        self.id=109
        try:
            self.bank=PersonalBanking(self.id)
        except NotACustomerException as e:
            print(e.args[0])
            return
        
    def transactions(self):
        return "No transactions to show here."
    
    def run(self):
        self.transactions()

#Demonstrating a new User
class User4(threading.Thread):
    def __init__(self):
        super().__init__()

    def get_new_account(self,name,opening_balance):
        bank=Banking()
        try:
            self.bank=bank.create_new_customer(name,opening_balance)
            self.bank.create_new_customer()
            self.name=name
            self.opening_balance=opening_balance
        except IllegalNameOrBalanceException as e:
            print(e.args[0])

    def transactions(self):
        self.bank.get_transaction_history()

    def run(self):
        self.get_new_account("Enid Blyton",9999)
        self.transactions()

#Bank server
class BankingServer:
    
    def __main__(self):
        user1 = User1()
        user2 = User2()
        user3 = User3()
        user4 = User4()
        user1.start()
        user2.start()
        user3.start()
        user4.start()
        user1.join()
        user2.join()
        user3.join()
        user4.join()
        print("Server is Idle...")

#start the server
server = BankingServer()
server.__main__()