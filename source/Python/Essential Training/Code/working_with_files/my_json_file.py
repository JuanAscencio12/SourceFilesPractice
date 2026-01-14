import json
from json import JSONDecodeError, JSONEncoder

class Animal:
    def __init__(self,name):
        self.name = name

class AnimalEncoder(JSONEncoder):
    def default(self, o):
        if type(o) == Animal:
            return o.name
        return super().default(o)

#JSON to Python
try:
    jsonString = '{"a": "apple", "b": "bear", "c": "cat",}'
    json.loads(jsonString)
    print(jsonString)
except JSONDecodeError as e:
    print(e)

#Python to JSON
pythonDict = {"a": "apple", "b": "bear", "c": "cat",}
print(json.dumps(pythonDict))

pythonDictAnimals = {"a": Animal("aardvark"), "b": Animal("bear"), "c": Animal("cat"),}
print(json.dumps(pythonDictAnimals, cls=AnimalEncoder))

