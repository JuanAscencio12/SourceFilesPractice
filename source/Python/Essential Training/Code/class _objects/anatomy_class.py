class Dog:
    _legs = 4
    def __init__(self, name):
        self.name = name

    def getLegs(self):
        return self._legs

    def speak(self):
        print(self.name + 'says: Bark!')
    
myDog = Dog('Rover')
myDog._legs = 3
print(myDog.name)
print(myDog.getLegs())
print(Dog._legs)