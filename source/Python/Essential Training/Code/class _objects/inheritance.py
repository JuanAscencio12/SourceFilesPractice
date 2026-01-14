class Dog:
    _legs = 4
    def __init__(self, name):
        self.name = name

    def getLegs(self):
        return self._legs

    def speak(self):
        print(self.name + 'says: Bark!')

class Chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says: Yap, yap, yap!')

    def wagTail(self):
        print('Vigorous wagging!')



myDog = Dog('Rover')
dog = Chihuahua('Roxy')

myDog.speak()
dog.speak()
dog.wagTail()

myList = list()

class UniqueList(list):
    def __init__(self):
        super().__init__()
        self.someProperty = 'Unique List'

    def append(self, item):
        if item in self:
            return
        super().append(item)

uniqueList = UniqueList()

uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)

print(uniqueList.someProperty)