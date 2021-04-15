# Complex
# 1) magic method (+, -, /, *)

class Complex:

    def __init__(self, chislo1, chislo2):
        self.chislo1 = chislo1
        self.chislo2 = chislo2

    def __add__(self, other):
        _sum_ = self.chislo1 + other.chislo2

    def __sub__(self, other):
        _sub_ = self.chislo1 - other.chislo2

    def __mul__(self, other):
        _mul_ = self.chislo1 * other.chislo2

    def __truediv__(self, other):
        _div_ = self.chislo1 / other.chislo2


a = complex(input('Ввод1:'))
b = complex(input('Ввод2:'))
Complex3 = a * b

print(Complex3)

# 2) return Complex ->
# complex2 = Complex(2, 5)
# complex3 = complex1 + complex2

class Complex0:

    def __init__(self, chislo1, chislo2):
        self.chislo1 = chislo1
        self.chislo2 = chislo2

    def __add__(self, other):
        chislo1 = self.chislo1 * other.chislo2 + self.chislo1 * other.chislo2
        chislo2 = self.chislo2 * other.chislo2
        return Complex0(chislo1, chislo2)

Complex1 = complex(2, 8)
Complex2 = complex(2, 5)
Complex3 = Complex1 + Complex2
print(Complex3)

# 3) __str__

class Stringi:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Dan - {self.name}"

Stringi1 = Stringi("Mashina")
print(Stringi1)
