class bank_account():
    def __init__(self):
        self.balance=0
        self.name = str(input("Enter your Name: \n"))
        self.acc_no = str(input("Enter your account no:-\n "))
        self.acc_type = str(input("Enter your account Type:-\n "))
    def deposit(self):


        amount=float(input("Enter the amount to be deposit :-\n"))
        self .balance=self.balance+amount

    def withdraw(self):
        amount = float(input("Enter the amount to be withdraw  :-\n"))
        if self.balance>=amount:
            print("\n You Withdraw:",amount)
            self.balance=self.balance-amount
        else:
            print("\nInsufficient balance")
    def display(self):
        print("Name: ",self.name)
        print("Acc No:- ",self.acc_no)
        print("Acc type :-",self.acc_type)
        print("\n Net Balance is :",self.balance)

s= bank_account()
s.deposit()
s.withdraw()
s.display()