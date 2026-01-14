'''
def square(num):
    someList = []
    for i in range(1,10)
        someList.append(i**2)
    return someList
'''

my_list = (n**2 for n in range(1,10))

#convert type
print(list(my_list))
print("---------")

my_list = (n**2 for n in range(1,10))
print(set(my_list))
print("---------")

my_list = (n**2 for n in range(1,10))
print(tuple(my_list))
print("---------")

#loop
my_list = (n**2 for n in range(1,10))
for num in my_list:
    print(num)
print("---------")

#next()
my_list = (n**2 for n in range(1,10))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))