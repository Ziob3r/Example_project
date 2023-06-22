class AnimalCare:
    def __init__(self, animal):
        self.animal = animal

    def care(self):
        self.feed_animal()
        self.play_with_animal()
        self.check_health()

    def feed_animal(self):
        print(f"Feeding {self.animal.name}")
        self.animal.eat()

    def play_with_animal(self):
        print(f"Playing with {self.animal.name}")

    def check_health(self):
        print(f"Checking health of {self.animal.name}")
