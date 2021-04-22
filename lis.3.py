class Engine:

    def __init__(self, hp, volume):
        self.hp = hp
        self.volume = volume

    def __str__(self):
        return f"hp: {self.hp}\nvolume: {self.volume}"


class Wheels:

    def __init__(self, diametr, season, protector, disk):
        self.diametr = diametr
        self.season = season
        self.protector = protector
        self.disk = disk


    def __str__(self):
        return f"diameter: {self.diametr}\nseason: {self.season}\nprotector: {self.protector}\ndisk: {self.disk}"

class Carcase:

    def __init__(self, material, farmat, color):
        self.material = material
        self.farmat = farmat
        self.color = color

    def __str__(self):
        return f"material: {self.material}\nfarmat: {self.farmat}\ncolor: {self.color}"


class Car:

    def __init__(self, wheels, engine, carcase):
        self.wheels = wheels
        self.engine = engine
        self.carcase = carcase

    def __str__(self):
        return f"Wheel: [{self.wheels}]\n\nEngine: [{self.engine}]\n\nCarcase: [{self.carcase}]"


wheel = Wheels(14, 'summer', 'bold', 'mattovyi')
engine = Engine(1500, 6)
carcase = Carcase('gold', 'sedan', 'glyans')

car = Car(wheel, engine, carcase)
print(car)
print(wheel)
print(engine)
print(carcase)