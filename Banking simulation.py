class Account:
    def __init__(self, ID,holder_name):
        self.ID=ID
        self.holder_name=holder_name
        self._balance=0 #encapsulation (private)
    def check_balance(self):
        return self._balance
    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
            print(f"Deposited {amount}. New balance is {self._balance}")
        else:
            print("Deposit amount must be a positive number.")
    def withdraw(self,amount):
        if self._balance>=amount:
            self._balance-=amount
            print(f"withdrawn {amount}. New balance is {self._balance}.")
        else:
            print("insufficie3nt balance.")

class Savings_Account(Account):
    def calculate_intrest(self,rate):
        intrest_rate=0.04
        intrest=self._balance*intrest_rate
        print(f"Intrest earned is {intrest}")

class Current_Account(Account):#inheritance
    def withdraw(self,amount): #Polymorphism
            Overdraft_Limit=1000
            if self._balance+Overdraft_Limit>=amount:
                self._balance-=amount
                print(f"withdrawn {amount}. New balance is {self._balance}.")
            else:
                print("insufficient balance.")

class Bank(Account):
    def __init__(self,name,city):
        self.name=name
        self.city=city
        self.__account={} #dictionary
    def create_account(self,ID,holder_name,type):
        if type=="Savings":
            new_account=Savings_Account(ID,holder_name)
        elif type=="Current":
            new_account=Current_Account(ID,holder_name)
        self.__account[ID]=new_account
        print("Account creation successful.")
        return new_account
    def get_account(self,ID):
        if ID not in self.__account:
            print("Account not found.")
        else:
            account=self.__account[ID]
            print(F"\nID:{account.ID}) .\n Holder_name:{account.holder_name}")
            return account

cbk=Bank("Chandan bank account of Karnataka","Mysore")
s1=cbk.create_account("369","Darshan","Savings")
c1=cbk.create_account("258","Chandan","Current")
s1.deposit(10000)
c1.deposit(50)
s1.withdraw(5000)
c1.withdraw(200)
s1.calculate_intrest(0.04)
s1.deposit(-1000)
s1.withdraw(12000)
c1.withdraw(3000)
cbk.get_account("444")
cbk.get_account("369")





