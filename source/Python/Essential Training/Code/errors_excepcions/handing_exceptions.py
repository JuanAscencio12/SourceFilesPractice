import time

def causeError():
    try:
        return 1/0
    except Exception as e:
        return e
    
def secondCauseError():
    try:
        return 1/0
    except Exception:
        print('There was some type of error!')

def thirdCauseError():
    start = time.time()
    try:
        time.sleep(0.5)
        return 1/0
    except Exception:
        print('There was some type of error!')
    finally:
        print(f'Function took {time.time() - start} seconds')
        
thirdCauseError()

##########################################################################################################

#Catching exceptions by type
def catchingExceptionsType():
    try:
        return 1 + 'a'
    except TypeError:
        print('There was as a TypeError!')
    except ZeroDivisionError:
        print("There waws a zero division error!")
    except Exception:
        print('There was some type of error!')
    finally:
        print("------------------------")

catchingExceptionsType()

##########################################################################################################

#Handle exceptions
def handleExceptions(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print('There was as zero division error!')
        except ZeroDivisionError:
            print("There waws a zero division error!")
        except Exception:
            print('There was some type of error!')
    return wrapper

@handleExceptions
def causeError():
    return 1/0

causeError()

##########################################################################################################

# Raising exceptions

@handleExceptions

def raiseError(n):
    if n == 0:
        raise Exception()
    print(n)

raiseError(1)