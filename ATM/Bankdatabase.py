from ATM.Account import CustomerAccount


class BankCustomerDatabase:
    def __init__(self):
        self.customeraccounts = [
            CustomerAccount(389012, 54321, 1000.0, 1200.0),
            CustomerAccount(389045, 12362, 1000.0, 1200.0)
    ]

    def getcustomeraccount(self, customeraccountnumber):
        for currentaccount in self.customeraccounts:
            if currentaccount.getcustomeraccountnumber() == customeraccountnumber:
                return currentaccount
        return None

    def authenticatecustomer(self, customeraccountnumber, customerpin):
        customeraccount = self.getcustomeraccount(customeraccountnumber)
        if customeraccount is not None:
            return customeraccount.checkandauthenticatepin(customerpin)
        else:
            return False

    def getcustomeravailablebalance(self, customeraccountnumber):
        return self.getcustomeraccount(customeraccountnumber).getcustomeravailablebalance()

    def getcustomertotalbalance(self, customeraccountnumber):
        return self.getcustomeraccount(customeraccountnumber).getcustomertotalbalance()

    def creditcustomeraccount(self, customeraccountnumber, amounttobeadded):
        return self.getcustomeraccount(customeraccountnumber).creditaccount(amounttobeadded)

    def debitcustomeraccount(self, customeraccountnumber, amounttoadded):
        return self.getcustomeraccount(customeraccountnumber).debitaccount(amounttoadded)

