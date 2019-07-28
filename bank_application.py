
import sys
class Customer:
    '''Customer class with bank related '''
    bankname='Punjab national bank'
    def __init__(self, name,balance=0):
        self.name=name
        self.balance=balance

    def deposit(self,atm):
        self.balance=self.balance+atm
        print('After deposit the balanced:',self.balance)

    def Withdraw(self,atm):
        if atm > self.balance:
            print('Insufficient fund..con not perform this operation')
            sys.exit()
        self.balance=self.balance-atm
        print('After withdraw balanced:',self.balance)

print('Welcome to',Customer.bankname)
name=input('Enter your name:')
c=Customer(name)

while True:
    print('d-Deposite\nw-Withdraw\ne-exit')
    option=input('Choose your option:')
    if option=='d' or option=='D':
        atm=float(input('Enter amount to deposit: '))
        c.deposit(atm)
    elif option=='w' or option=='W':
        atm=float(input('Enter amount to withdraw: '))
        c.Withdraw(atm)
    elif option=='e' or option=='E':
        print('Thank for banking')
        sys.exit()
    else:
        print('Choose valid option')