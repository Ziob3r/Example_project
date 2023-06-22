from animal import Dog, Cat
from person import Person
from animal_care import AnimalCare
from person_data import PersonData
from same_name_class1 import SameNameClass as SameNameClass1
from same_name_class2 import SameNameClass as SameNameClass2
from mydatetime import MyDateTime

class Application:
    def __init__(self):
        # Stworzenie obiektów
        self.dog = Dog("Rex", "Golden Retriever")
        self.cat = Cat("Felix", "Siamese")
        self.person = Person("John")
        self.animal_care = AnimalCare(self.dog)
        self.person_data = PersonData("John", 30, "1234 Some Street")
        self.same_name_class1 = SameNameClass1(5)
        self.same_name_class2 = SameNameClass2(10, 20)
        self.my_datetime = MyDateTime.now()

    def run(self):
        # Używanie obiektów
        print(self.dog.speak())
        print(self.cat.speak())
        print(self.person.greet())
        self.animal_care.care()
        print(self.person_data.name, self.person_data.age, self.person_data.address)
        print(self.same_name_class1.action())
        print(self.same_name_class1.print_class_info())
        print(self.same_name_class1.utility_method(10))
        print(self.same_name_class2.action())
        print(self.same_name_class2.print_class_info())
        print(self.same_name_class2.utility_method(10, 20))
        print(self.my_datetime.formatted())

        self.person.add_pet(self.dog)
        self.person.add_pet(self.cat)
        self.person.show_pets()