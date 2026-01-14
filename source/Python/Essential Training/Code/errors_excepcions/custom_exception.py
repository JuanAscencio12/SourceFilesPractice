'''
class CustomException(Exception):
    pass

def causeError():
    raise CustomException('You called the causeError function')

causeError()
'''

class HttpException(Exception):
    statusCode = None
    message = None
    def __init__(self):
        super().__init__(f'Status code {self.statusCode} and message is: {self.message}')

class NotFound(HttpException):
    statusCode = 404
    message = 'Resourcce not found'


class ServerError(HttpException):
    statusCode = 500
    message = 'The server messed up!'

def raiseServerError():
    raise ServerError()

try:
    raiseServerError()
except HttpException as e:
    print(e)