class fruit:
    def __init__(self, color, taste) -> None:
        self.color = color #instance variable
        self.taste = taste #instance variable

#creating objects with unnique attributes
banana = fruit('yellow', 'sweet')
lemon = fruit('yellow', 'sour')

print(banana.color)
print(lemon.taste)