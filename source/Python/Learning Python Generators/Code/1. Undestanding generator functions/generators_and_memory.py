# Throws intencionaly an error
def X_all_the_nums():
    list_nums = []
    num = 0
    while(True):
        list_nums.append(num)
        num += 1
    
# Generator
def all_the_nums():
    num = 0
    while(True):
        yield num
        num += 1

for num in all_the_nums():
    print(num)