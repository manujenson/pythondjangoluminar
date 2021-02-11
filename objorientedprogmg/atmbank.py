class bank:
    def bal_enq(self):
        print("inside bal enqury")
    def withdraw(self):
        print("inside withdraw")
    def __deposit(self):
        print("inside deposit")


obj=bank()
obj._bank__deposit()