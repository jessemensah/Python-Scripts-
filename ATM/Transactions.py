from abc import ABC, abstractmethod


class Transactions(ABC):
    def __init__(self, customeraccountnumber, atmscreen, atmcustomerbankdatabase):
        self.accountnumber = customeraccountnumber
        self.screen = atmscreen
        self.bankdatabase = atmcustomerbankdatabase

    def getcustomeraccountnumber(self):
        return self.accountnumber

    def getatmscreen(self):
        return self.screen

    def getcustomerbankdatabase(self):
        return self.bankdatabase

    @abstractmethod
    def execute(self):
        pass
