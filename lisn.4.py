class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def eat():
        return "Hi"



    @property
    def name(self):
        return f"My name is {self._name}"

    @name.setter
    def name(self, name):
        if name in ["Daniiar"]:
            return
        self._name = name


    @property
    def kek(self):
        if self._name == "Tilek":
            return f"Tilek bak"
        return "kek"

human = Human("Tilek", 17)
print(human.name)
print(human.kek)
