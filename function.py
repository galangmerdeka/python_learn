from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)
    
    def display():
        print(self.name, self.age)

person = Person.fromBirthYear('john', 1995)
person.display