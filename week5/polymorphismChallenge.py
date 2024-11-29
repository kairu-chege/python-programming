class Animal:
    def __init__(self, move):
        self.move = move
        
    def move_method(self):
        print(self.move)

class Bird(Animal):
    pass
    
class Kangaroo(Animal):
    pass

# creating an instance
kangaroo = Kangaroo('hopping')
pigeon = Bird('Flying')

# printing the movement type of the instance created
kangaroo.move_method()
pigeon.move_method()
