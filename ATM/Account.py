class CustomerAccount:
    def __init__(self, customeraccountnumber, customerpin, customeravailablebalance, customertotalbalance):
        self.customeraccountnumber = customeraccountnumber
        self.customerpin = customerpin
        self.customeravailablebalance = customeravailablebalance
        self.customertotalbalance = customertotalbalance

    def checkandauthenticatepin(self, customer_pin):
        return customer_pin == self.customerpin

    def getcustomeravailablebalance(self):
        return self.customeravailablebalance

    def getcustomertotalbalance(self):
        return self.customertotalbalance

    def creditaccount(self, amounttobeadded):
        self.customertotalbalance += amounttobeadded

    def debitaccount(self, amounttotakeout):
        self.customeravailablebalance -= amounttotakeout
        self.customertotalbalance -= amounttotakeout

    def getcustomeraccountnumber(self):
        return self.customeraccountnumber
