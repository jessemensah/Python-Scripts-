from ATM.Transactions import Transactions
from BalanceInquiry import CustomerBalanceInquiry
from Withdrawal import Withdrawal
from Deposit import CustomerDeposit
from DepositSlot import ATMDepositSlot
from Screen import Screen
from Keypad import ATMKeypad
from CashDispenser import ATMCashDispenser
from Bankdatabase import BankCustomerDatabase

class ATM:
    BALANCE_INQUIRY = 1
    WITHDRAWAL = 2
    DEPOSIT = 3
    EXIT = 4


    def __init__(self):
        self.userauthenticated = False
        self.currentaccountnumber = 0
        self.screen = Screen()
        self.keypad = ATMKeypad()
        self.cashdispenser = ATMCashDispenser()
        self.depositslot = ATMDepositSlot()
        self.bankdatabase = BankCustomerDatabase()

    def displaymainmenu(self):
        self.screen.displayscreenmessageline("\nMain Menu")
        self.screen.displayscreenmessageline("1 - View my balance")
        self.screen.displayscreenmessageline("2 - Withdraw Cash")
        self.screen.displayscreenmessageline("3 - Deposit Funds")
        self.screen.displayscreenmessageline("Enter a choice")
        return self.keypad.getcustomerinput()

    def authenticateuser(self):
        self.screen.displayscreenmessage("\nPlease enter your account number: ")
        customeraccountnumber = self.keypad.getcustomerinput()
        self.screen.displayscreenmessage("Enter your PIN: ")
        pin = self.keypad.getcustomerinput()

        self.userauthenticated = self.bankdatabase.authenticatecustomer(customeraccountnumber, pin)

        if self.userauthenticated:
            self.currentaccountnumber = customeraccountnumber
        else:
            self.screen.displayscreenmessageline("Invalid account number or PIN.Please try again")


    def createtransaction(self, transactiontype):
        transaction = None

        if transactiontype == self.BALANCE_INQUIRY:
            transaction = CustomerBalanceInquiry(self.currentaccountnumber, self.screen, self.bankdatabase)
        elif transactiontype == self.WITHDRAWAL:
            transaction = Withdrawal(self.currentaccountnumber. self.screen, self.cashdispenser, self.bankdatabase, self.keypad)
        elif transactiontype == self.DEPOSIT:
            transaction = CustomerDeposit(self.currentaccountnumber, self.screen, self.bankdatabase, self.keypad, self.depositslot)
        return transaction

    def performtransaction(self):
        currenttransaction = Transactions()
        customerexited = False

        while not customerexited:
            customermenuselection = self.displaymainmenu()

            if customermenuselection in [self.BALANCE_INQUIRY, self.WITHDRAWAL, self.DEPOSIT]:
                currenttransaction = self.createtransaction(customermenuselection)
                currenttransaction.execute()
            elif customermenuselection == self.EXIT:
                self.screen.displayscreenmessageline("\nExiting the system...")
                customerexited = True
            else:
                self.screen.displayscreenmessageline("\nYou did not enter a valid selection. Try Again")

    def run(self):
        while True:
            while not self.userauthenticated:
                self.screen.displayscreenmessageline("\nWelcome!")
                self.authenticateuser()
            self.performtransaction()
            self.userauthenticated = False
            self.currentaccountnumber = 0
            self.screen.displayscreenmessageline("\nThank You!. GoodBye")




















