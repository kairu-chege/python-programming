
class Pet: #parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
        
    def speak(self):
        print("I don't know what to say")
    
class Cat(Pet):  #child class
    def speak(self):
        print("Meow")
        
class Dog(Pet):  #child class
    def speak(self):
        print("Bark")

class Fish(Pet):  #child class
    pass
p = Pet("Fifi", 12)
p.show()
c = Cat("puss", 4)
c.speak()
d = Dog("wile", 20)
d.show()
f = Fish("Nemo", 3)
f.speak()