class BancAccount:

    def __init__(self, _name, _balance):
        self.name = _name
        self.balance = _balance

    @property
    def name(self):
        return f"My accaunt:{self.name}"

    @name.setter
    def name(self):
        return self.name


    @property
    def balance(self):
        return f"My balance:{self.balance}"

    @balance.setter
    def balance(self, balance):
        if self.balance > 0:
            return self.balance
        else:
            print(None)


account = BancAccount("Adil", 9000)
account.balance = - 95
account.name = "Malik"
print(account.name)
print(account.balance)
