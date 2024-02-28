class Cat:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def getmeow(self):
        return f"The cat {self.name}, {self.age} years old says 'Meow!'."


cat_1 = Cat('Молі', 3)
print(cat_1.getmeow())