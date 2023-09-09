from Transactions import Transactions

class CustomerBalanceInquiry(Transactions):
    def __init__(self, customeraccountnumber, atmscreen, atmcustomerbankdatabase):
        super().__init__(customeraccountnumber, atmscreen, atmcustomerbankdatabase)

    def execute(self):
        bankcustomerdatabase = self.getcustomerbankdatabase()
        screen = self.getatmscreen()
        customeravailablebalance = bankcustomerdatabase.getcustomeravailablebalance(self.getcustomeraccountnumber())
        customertotalbalance = bankcustomerdatabase.getcustomertotalbalance(self.getcustomeraccountnumber())

        screen.displayscreenmessageline("\nBalance Information")
        screen.displayscreenmessage(" Available balance ")
        screen.displaypoundamount(customeravailablebalance)
        screen.displayscreenmessage("\n Total Balance:    ")
        screen.displayscreenmessageline("")

