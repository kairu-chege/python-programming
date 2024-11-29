#class attributes are specific to a class not to an instance

class Person:
    number_of_people = 0
    
    def __init__(self, name):
        self.name = name
        Person.add_person()
    
    @classmethod  
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("tina")
p2 = Person("yass")
print(Person.number_of_people_())