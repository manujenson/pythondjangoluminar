#withdrwl,deposit,balance,create accnt

from datetime import datetime

class bank:
    bank_name="sbi"

    def __init__(self,accno,name,balance):
        self.accno=accno
        self.p_name=name
        self.balance=balance


    def deposit(self,amount):
        self.balance+=amount

        print(bank.bank_name,"your acnt ",self.accno,"has been credited with ",amount,"on",datetime.today(),"balance is",self.balance)

    def withdrawal(self,amount):

        if self.balance > amount:
            self.balance-=amount
            print("ur acnt",self.accno,"has been credited with amount",amount,"on",datetime.today(),"balance is",self.balance)

        else:
            print("insuficient balance")

    def balance(self):
        print(self.balance)

obj=bank(1000,"manu",3000)


obj.deposit(10000)
