import time
import os

def all_primes_up_to(number):
    primeList = [2]

    for num in range(3,number+1):
        sqrtNum = num ** 0.5
        for factor in primeList:
            if num % factor == 0:
                break
            if factor > sqrtNum:
                primeList.append(num)
                break
    
    return primeList


while True:
    try: 
        number = int(input("Number: "))
        break
    except ValueError:
        print("Error de valor")
        time.sleep(1)
        os.system('cls')

print(all_primes_up_to(number))
oneChance = False

#REVISAR CRIBA DE ERATOSTENES


for n in range(2,101):
    for factor in range(2,int(n ** 0.5)+1):
        if n % factor == 0:
            break
    else:
        print(f"{n} is prime!")