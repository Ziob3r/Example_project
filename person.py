from animal import Dog, Cat

class Person:
    pets = []  # Zmienna klasowa

    def __init__(self, name):
        self.name = name  # Zmienna instancyjna

    @classmethod
    def add_pet(cls, pet):
        cls.pets.append(pet)

    @staticmethod
    def greet():
        return "Hello!"

    def show_pets(self):
        for pet in self.pets:
            print(pet.name)
