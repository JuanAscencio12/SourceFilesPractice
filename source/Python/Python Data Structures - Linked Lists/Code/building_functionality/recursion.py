# Recursion IS NOT a great solution for linked lists

def factorial(num):
    if num <= 0:
        return 'Not possible'
    if num == 1:
        return 1
    return num * factorial(num-1)

print(factorial(999)) #limit 1000