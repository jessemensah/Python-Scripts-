from Transactions import Transactions
from Keypad import ATMKeypad
from Bankdatabase import BankCustomerDatabase
from CashDispenser import ATMCashDispenser


class Withdrawal(Transactions):
    CANCELEDTRANSACTION = 6
    atmKeypad = ATMKeypad()
    cashDispenser = ATMCashDispenser()

    def __init__(self, customeraccountnumber, atmscreen, atmcashdispenser, atmbankdatabase, atmkeypad):
        super().__init__(customeraccountnumber, atmscreen, atmbankdatabase)
        self.amount = 0.0
        self.cashdispenser = atmcashdispenser
        self.keypad = atmkeypad

    def execute(self):
        cashDispensed = False
        customeravailableabalance = 0.0
        customerbankdatabase = BankCustomerDatabase()

        screen = self.screen()

        while not cashDispensed:
            self.amount = self.displaymenuofamounts()

            if self.amount != self.CANCELEDTRANSACTION:
                customeravailableabalance = customerbankdatabase.getcustomeravailablebalance(
                    self.getcustomeraccountnumber())

                if self.amount <= customeravailableabalance:
                    if self.cashDispenser.sufficientcustomermoneyavailable(self.amount):
                        customerbankdatabase.debitcustomeraccount(self.getcustomeraccountnumber(), self.amount)
                        self.cashDispenser.dispensecustomercash(self.amount)
                        cashDispensed = True
                        screen.displayscreenmessageline("\nYour cash has been dispensed. Please take your cash now")
                    else:
                        screen.displayscreenmessageline("\nInsufficient cash available in the ATM."
                                                        "\n\nPlease choose a smaller amount")
                else:
                    screen.displayscreenmessageline("\nInsufficient cash available in your account."
                                                    "\n\nPlease choose a smaller amount")
            else:
                screen.displayscreenmessageline("\nCanceling transactions...")
                return

    def displaymenuofamounts(self):
        customerchoice = 0
        screen = self.getatmscreen()
        amounts = [0, 20, 40, 60, 100, 200]

        while customerchoice == 0:
            screen.displayscreenmessageline("\nWithdrawal Menu: ")
            screen.displayscreenmessageline("1 - £20")
            screen.displayscreenmessageline("1 - £40")
            screen.displayscreenmessageline("2 - £60")
            screen.displayscreenmessageline("3 - £100")
            screen.displayscreenmessageline("4 - £200")
            screen.displayscreenmessageline("\nChoose a withdrawal amount: ")

            inputvalue = self.atmKeypad.getcustomerinput()

            if 1 <= inputvalue <= 5:
                customerchoice = amounts[inputvalue]
            elif inputvalue == self.CANCELEDTRANSACTION:
                customerchoice = self.CANCELEDTRANSACTION
            else:
                screen.displayscreenmessageline("\nInvalid Selection. Try Again")
        return customerchoice
