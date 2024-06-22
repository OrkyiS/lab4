class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Bicycle(Product):
    def __init__(self, name, price, brand):
        super().init(name, price)
        self.brand = brand

class MountainBike(Bicycle):
    def __init__(self, name, price, brand, suspension):
        super().init(name, price, brand)
        self.suspension = suspension

class Scooter(Product):
    def __init__(self, name, price, wheels):
        super().init(name, price)
        self.wheels = wheels

class Animal:
    def __init__(self, species):
        self.species = species

class Bird(Animal):
    def __init__(self, species, wingspan):
        super().init(species)
        self.wingspan = wingspan

class Tit(Bird):
    def __init__(self, species, wingspan, color):
        super().init(species, wingspan)
        self.color = color

class Lion(Animal):
    def __init__(self, species, mane_length):
        super().init(species)
        self.mane_length = mane_length

class Dolphin(Animal):
    def __init__(self, species, speed):
        super().init(species)
        self.speed = speed