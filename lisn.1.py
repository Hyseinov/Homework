class fraction:

    def __init__(self, chislitel, znamenatel):
        self.chislitel = chislitel
        if znamenatel == 0:
            raise ValueError("nepravilno")
        self.znamenatel = znamenatel

    def add(self, other):
        chislitel = self.chislitel * other.znamenatel + self.chislitel * other.znamenatel
        znamenatel = self.znamenatel * other.znamenatel

        print(chislitel)
        print('__')
        print(znamenatel)

Fraction1 = fraction(1, 2)
Fraction2 = fraction(1, 8)
Fraction1.add(Fraction2)
