def x():
    return 5

def removeNewLines(text):
    text = text.replace('\n','')
    return text

def removeShortWords(text):
    return ''.join(word for word in text.split() if len > 3)

def removeLongWords(text):
    return ''.join(word for word in text.split() if len < 6)

procesing_functions = [removeNewLines, removeShortWords, removeLongWords]

print(x.__code__.co_varnames)
print(x.__code__.co_code)

myList = [23,313,124,26,4,433]
mySecondList = [{'num': 2},{'num': 3},{'num': 1}]

print((lambda x: x + 3)(5))
print(sorted(myList))
print(sorted(mySecondList, key=lambda x: x['num']))
