
class Bank:
    def get_interest_rate(self):
        return 0


class SBI(Bank):
    def get_interest_rate(self):
        return 6.5


class HDFC(Bank):
    def get_interest_rate(self):
        return 7.0


class ICICI(Bank):
    def get_interest_rate(self):
        return 6.8


banks = [SBI(), HDFC(), ICICI()]

for bank in banks:
    print(type(bank).__name__,
          "Interest Rate:", bank.get_interest_rate(), "%")
