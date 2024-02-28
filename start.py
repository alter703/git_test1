class Cat:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def getmeow(self):
        return f"The cat {self.name}, {self.age} years old says 'Meow!'."

    def log_cat(self):
        return {'name': self.name, 'age': self.age}


if __name__ == '__main__':
    cat_1 = Cat('Молі', 3)
    print(cat_1.getmeow())
