'''
Local variables
'''
def performOperation(*args, **kwargs):
    print(args)
    print(kwargs)


def perform_operation_locale(num1, num2, operation='sum'):
    print(locals())

performOperation(1,2,3, operation="sum")
perform_operation_locale(1,2,operation="multiply")

'''
Global variables
'''
#print(globals())

'''
Scope
'''
message = 'Some global data'

def function1(varA, varb):
    print(message)
    def inner_function(varA, varB):
        print(f'inner_function local scope: {locals()}')

    print(locals())
    inner_function(123,456)


def function2(varC, varB):
    print(message)
    print(locals())

function1(1,2)
function2(3,4)