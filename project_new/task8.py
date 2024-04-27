SPACE = " "
STAR = '*'
ONE = 1
rows = int(input('Сколько рядов у елки?: '))
spaces = rows - ONE
stars = ONE

for i in range(rows):
    print(spaces * SPACE + stars * STAR)
    spaces -=1
    stars +=2
