class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('my name is ' + self.name + ' and my age is' + str(self.age))

    def make_sound(self):
        print("Meow meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('my name is ' + self.name + ' and my age is ' +str(self.age))

    def make_sound(self):
        print("Bow wow")

def my_pet(pet):
    pet.info()
    pet.make_sound()

c = Cat("Ringo", 2)
d = Dog("Tucker", 3)

my_pet(c)