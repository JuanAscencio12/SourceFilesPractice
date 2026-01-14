myList = [1,2,3,4]
animalLookup = {
    'a': ['aardvard', 'antelope'],
    'b': ['bear'],
    'c': ['cat'],
    'd': ['dog'],
}

for item in myList:
    print(item)


for letter, animal in animalLookup.items():
    pass

for letter, animal in animalLookup.items():
    if len(animal) > 1:
        continue
    print(f'Only one animal! {animal}')

for letter, animal in animalLookup.items():
    if len(animal) > 1:
        print(f"Found {len(animal)} animals: {animal}")
        break


#For else
for number in range(2,100):
    for factor in range(2, int(number ** 0.5) + 1):
        if number % factor == 0:
            break
    else:
        print(f'{number} is prime!')


#Same as fore else
for number in range(2,100):
    found_facors = False
    for factor in range(2,int(number**0.5)+1):
        if number % factor == 0:
            found_facors = True
            break
    if not found_facors:
        print(f'{number} is prime')