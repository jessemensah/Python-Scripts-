class ATMCashDispenser:
    INITIAL_COUNT = 500

    def __init__(self):

        # Instance variables to track count of notes
        self.count = self.INITIAL_COUNT

        # Simulates dispense cash
    def dispensecustomercash(self, amounttodispense):
        billsrequired = amounttodispense // 20
        self.count -= billsrequired

    def sufficientcustomermoneyavailable(self, amountavailable):
        billsrequired = amountavailable // 20
        return self.count >= billsrequired
