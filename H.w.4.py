class BancAccount:

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    @property
    def name(self):
        return f"My accaunt:{self._name}"


    @property
    def balance(self):
        if self._balance < 0:
            print(None)
        else:
            return f"My balance:{self._balance}"



account = BancAccount("Adil", 9000)
account._balance = -95

print(account.name)
print(account.balance)
