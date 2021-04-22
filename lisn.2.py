class Animal:

    def __init__(self, eyes, tongue, ears):
        self.eyes = eyes
        self.tongue = tongue
        self.ears = ears


    def run(self):
            return 'Run to Donkey'


class Donkey(Animal):

    def __init__(self, eyes, tongue, ears, tail):
        super(Donkey, self).__init__(eyes, tongue, ears)
        self.tail =tail



class Eshek(Donkey):

    def __init__(self, eyes, tongue, ears, tail, stamina):
        super(Eshek, self).__init__(eyes, tongue, ears, tail)
        self.stamina = stamina


class osyol(Donkey):

    def __init__(self, eyes, tongue, ears, tail, stubborn):
        super(osyol, self).__init__(eyes, tongue, ears, tail)
        self.stubborn = stubborn


    def run(self):
        return 'Ran to Eshak'


donkey = Donkey('big', 'long', 'dis', 'short')
print(donkey.run())

Osyol = osyol('big', 'long', 'dis', 'short', True)
print(osyol.run)




