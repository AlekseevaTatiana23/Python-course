# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

LOW_LIMIT = 1
UPPER_LIMIT = 100000

num = LOW_LIMIT - 1
counter = 0

while num < LOW_LIMIT:
    num = int(input(f'Введите число от {LOW_LIMIT} до {UPPER_LIMIT}: '))


for i in range(1, num+1):
    if num % i == 0:
        counter += 1
print('Простое число' if counter == 2 else 'Составное число')