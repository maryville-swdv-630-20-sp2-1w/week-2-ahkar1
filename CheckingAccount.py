
class CheckingAccount:
    def __init__ (self, name, address, accountnumber, balance):
     self._balance = balance
     self.name = name
     self.address = address
     self.accountnumber = accountnumber
    
    def credit(self, trans):
        newbalance = self._balance + trans
        
        self._balance = newbalance
        
    def debit(self, trans):
        newbalance = self._balance - trans
        self._balance = newbalance
    def getBalance(self):
        return self._balance
    def statement(self):
        print(self.name)
        print(self.address)
        print("Account Number  : % 3d" %(self.accountnumber))
        print("Account Balance : ${:,.2f}".format(self._balance))

        
def main():
    account = CheckingAccount('Matthias Pupillo','123 Main St', 3432342234, 100000)
    print("Credit $500")
    account.credit(500)
    print("Account Balance : ${:,.2f}".format(account.getBalance()))
    print("Debit $300")
    account.debit(300)
    print("Account Balance : ${:,.2f}".format(account.getBalance()))
    print("Credit $500")
    account.credit(200)
    print("Account Balance : ${:,.2f}".format(account.getBalance()))
    print("Debit $3000")
    account.debit(3000)
    print("Account Balance : ${:,.2f}".format(account.getBalance()))
    print("Statement\n")
    account.statement()
    
main()