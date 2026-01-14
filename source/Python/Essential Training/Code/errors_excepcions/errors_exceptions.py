'''
def causeError():
    return 1 / 0

def callCauseError():
    return causeError()

causeError()
#Stacktrace the output
'''

try:
    1/0
except Exception as e:
    print(type(e))