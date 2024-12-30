import threading
import datetime
import pandas as pd

from banking_errors import InsufficientBalanceException, NotACustomerException, ZeroOrNegativeDepositException

class BankingServer(threading.Thread):
    #simulate a real-time banking server
    pass

class Banking:

    def __init__(self):
        self.customer_data=pd.read_csv('data.csv')

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
        #print("Balance Updated...")

    def transaction_history(self):
        pass


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
        self.id=self.data["CustomerID"]
        self.name=self.data["Name"]
        self.balance=self.data["AccountBalance"]

    def deposit(self, amount):
        try:
            self.balance = super().deposit(self.id,balance_lock,self.balance,amount)
            self.update_transaction_history("deposited",amount)
        except ZeroOrNegativeDepositException as e:
            self.update_transaction_history("A Failed Deposit",0)
            print(e.args[0])

    def withdraw(self, withdrawal_amount):
        try:
            self.balance = super().withdraw(self.id,balance_lock,self.balance,withdrawal_amount)
            self.update_transaction_history("withdrawn",withdrawal_amount)
        except InsufficientBalanceException as e:
            self.update_transaction_history("A Failed Withdrawal",0)
            print(e.args[0])

    def update_transaction_history(self,action,amount):
        update=f"{datetime.datetime.now()}: {amount} was {action}. New balance is {self.balance}"
        transaction_history.append(update)

    def get_transaction_history(self):
        for transaction in transaction_history:
            print(transaction)

try:
    person1 = PersonalBanking(109)
    person1.withdraw(1000)
    person1.deposit(900)
    person1.get_transaction_history()
except NotACustomerException as e:
    print(e.args[0])

print("================================")

try:
    person2 = PersonalBanking(102)
    person2.withdraw(1000)
    person2.deposit(10000)
    person2.get_transaction_history()
except NotACustomerException as e:
    print(e.args[0])
