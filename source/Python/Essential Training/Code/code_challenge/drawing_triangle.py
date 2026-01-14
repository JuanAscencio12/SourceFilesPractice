heigth = int(input('Enter your heigth: '))
width = 2 * heigth

for i in range(heigth):
    triangleWidth = 2 * i + 1
    padding = int((width - triangleWidth)/2)
    print(' ' * padding + '*' * triangleWidth)