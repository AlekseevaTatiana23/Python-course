# Представить целое число в двоичной и восьмиричной системе счисления

DIV_BIN = 2
DIV_OCT = 8

original_num: int = int(input('Введите целое число: '))
for div in (DIV_BIN, DIV_OCT):
    num = original_num
    result: str = ''
    while num:
        result = str(num % div) + result
        num //= div
    print(f'Число {original_num} в {div} системе {result}')
