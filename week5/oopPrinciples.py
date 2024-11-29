# inheritance 

class Vehicle: #parent class
    def __init__(self, wheels) -> None:
        self.wheels = wheels
        
class Car(Vehicle): #child class to inherit the parent class wheels attribute
    pass

class Bicycle(Vehicle): #child class
    pass

Car = Car(4)
Bicycle = Bicycle(2)

print(f'A car has {Car.wheels} wheels.')
print(f'A bicycle has {Bicycle.wheels} wheels.')

#polymorphism
class Dog:
    def speak(self):
        return 'woof'
    
class Cat:
    def speak(self):
        return 'meow'
    
#polymorphism in action
for animal in [Dog(), Cat()]:
    print(animal.speak())
    
#Encapsulation
class SecretStash:
    def __init__(self) -> None:
        self.__chocolates = 10  #private attribute
        
    def take_chocolate(self): # public method to access the private attribute and modify its value
        if self.__chocolates > 0:
            self.__chocolates -= 1
            print('One chocolate taken!')
        else:
            print('No chocolates left')
            
stash = SecretStash()
stash.take_chocolate()