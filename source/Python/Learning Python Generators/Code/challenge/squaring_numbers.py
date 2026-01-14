from os import system

def clear():
    system('pause')
    system('cls')

def squararing_numbers(integer):
    for num in range(1,integer+1):
            yield num**2

def main():
    integer = 0
    
    while(True):    
        try:
            integer = int(input("Introduce an integer: "))
            break
        except ValueError as e:
            print(e)
            clear()
        except:
            print("Something went wrong")
            clear()

    print(list(squararing_numbers(integer)))

if __name__ == "__main__":
    main()