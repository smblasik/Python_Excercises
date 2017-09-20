class Account:

    def __init__(self,filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self,amount):
        self.balance=self.balance-int(amount)

    def deposit(self,amount):
        self.balance=self.balance+int(amount)

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):

    """This class generates checking account ojbects"""

    type="checking"

    def __init__(self,filepath,fee):
        self.fee=fee
        Account.__init__(self,filepath)

    def transfer(self,amount):
        self.balance=self.balance-amount-self.fee


jacks_checking=Checking("balance.txt",1)
jacks_checking.transfer(110)
print(jacks_checking.balance)
jacks_checking.commit()

johns_checking=Checking("balance.txt",1)
johns_checking.transfer(110)
print(johns_checking.balance)
johns_checking.commit()
