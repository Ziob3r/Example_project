class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

    def eat(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"

    def eat(self):
        return "Eating dog food"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return "Meow!"

    def eat(self):
        return "Eating cat food"
