LOW_LIMIT = 1
UPPER_LIMIT = 999
TEN = 10
HUNDRED = 100

num = LOW_LIMIT - 1

while num < LOW_LIMIT or num > UPPER_LIMIT:
    num = int(input(f'Введите число от {LOW_LIMIT} до {UPPER_LIMIT}: '))

if num < TEN:
    result = f'Число {num} цифра. Ее квадрат равен {num * num}'
elif num < HUNDRED:
    f_num = num // TEN
    s_num = num % TEN
    result = f'Число {num} двузначное. Произведение цифр равно {f_num * s_num}'
else:
    f_num = num // HUNDRED
    s_num = num // TEN % TEN
    t_num = num % TEN
    result = f'Число {num} трехзначное. Зеркальное отображение {t_num * HUNDRED + s_num * TEN + f_num}'
print(result)
