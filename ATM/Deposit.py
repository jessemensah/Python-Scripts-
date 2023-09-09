from Transactions import Transactions
from Keypad import ATMKeypad
from DepositSlot import ATMDepositSlot
from Bankdatabase import BankCustomerDatabase


class CustomerDeposit(Transactions):
    CANCELEDTRANSACTION = 0
    atmkeypad = ATMKeypad()
    depositSlot = ATMDepositSlot()

    def __init__(self, customeraccountnumber, atmscreen, atmcustomerbankdatabase, atmkeypad, atmdepositslot):
        super().__init__(customeraccountnumber, atmscreen, atmcustomerbankdatabase)
        self.amount = 0.0
        self.keypad = atmkeypad
        self.depositslot = ATMDepositSlot()

    def askfordepositamount(self):
        screen = self.getatmscreen()
        screen.displayscreenmessage("\nPlease enter a deposit amount in CENTS (or 0 to cancel): ")
        inputvalue = self.atmkeypad.getcustomerinput()
        if inputvalue == self.CANCELEDTRANSACTION:
            return self.CANCELEDTRANSACTION
        else:
            return float(inputvalue) / 100

    def execute(self):
        customerbankdatabase = BankCustomerDatabase()
        screen = self.getatmscreen()
        self.amount = self.askfordepositamount()
        if self.amount != self.CANCELEDTRANSACTION:
            screen.displayscreenmessage("\nPlease insert a deposit envelope containing ")
            screen.displaypoundamount(self.amount)
            screen.displayscreenmessageline(".")

            enveloperecieved = self.depositSlot.isenveloperecieved()

            if enveloperecieved:
                screen.displayscreenmessage("\nYour envelope has been received.\nNOTE: The money just deposited will "
                                            "not"
                                            "be available until we verify the amount of any "
                                            "enclosed cash and your checks later"
                )
                customerbankdatabase.creditcustomeraccount(self.getcustomeraccountnumber(), self.amount)
            else:
                screen.displayscreenmessage("\nCanceling transactions...")
