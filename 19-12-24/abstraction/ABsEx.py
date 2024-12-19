from abc import ABC,abstractmethod

class Accounts:
    def savings(self):
        print("Zero Balance Account")

class Loans(ABC):
    @abstractmethod
    def pl(self):
        pass

class Final(Loans,Accounts):
    def pl(self):
        print("Personal Loans")

ob1= Final()
ob1.savings()
ob1.pl()