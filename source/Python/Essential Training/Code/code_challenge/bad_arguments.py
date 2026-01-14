# Python code​​​​​​‌‌‌​​​‌​‌​​‌​‌​​​​​‌​​‌‌‌ below
class NonIntArgumentException(Exception):
    def __init__(self):
        super().__init__('One of the arguments isn\'t an integer')

def handleNonIntArguments(func):
    def wrapper(*args):
        for arg in args:
            if type(arg) is not int:
                raise NonIntArgumentException()
        return func(*args)
    return wrapper


@handleNonIntArguments
def sum(a, b, c):
    return a + b + c

try:
    result = sum(1, 2, 3)
    print(result)
except NonIntArgumentException as e:
    print(e)

try:
    result = sum(1.0, 2.0, 3.0)
    print(result)
except NonIntArgumentException as e:
    print(e)

try:
    result = sum(None, None, None)
    print(result)
except NonIntArgumentException as e:
    print(e)