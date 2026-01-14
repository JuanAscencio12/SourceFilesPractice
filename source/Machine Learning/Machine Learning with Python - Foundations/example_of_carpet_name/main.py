import os

def cls():
    os.system("cls")

def pause():
    os.system("pause")

def main():
    times = 5
    while True:
        user = input("User: ")
        password = input("Password: ")
        
        if times != 0:
            if user == "Juan" and password == "456":
                cls()
                break
            else:
                times -= 1
                print("Wrong input, try again.")
                pause()
                cls()
        else:
            print("Contact your supervisor.")
            return

    while True:
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        try:
            option = int(input("Option: "))
        except:
            print("Not valid option.")
            pause()
            cls()
            


    


if __name__ == "__main__":
    cls()
    main()