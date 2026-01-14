# Give a square of a number using triangle numbers
def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def squareFunc(num):
    sq = triangle(num) + triangle(num-1)
    return sq

number_50 = squareFunc(50)
print(number_50)