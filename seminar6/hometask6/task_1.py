'''
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.

В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
'''

__all__ = ['date_is_true']
from sys import argv

def _is_leap(year:int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
def date_is_true(data: str) -> bool:
    day, month, year = map(int, data.split('.'))
    check_days = {
        1:31,
        2:29 if _is_leap(year) else 28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
        }
    max_day = check_days.get(month)
    if not max_day or (year > 9999 or year < 1) or (day > max_day or day < 1):
        return False
    else:
        return True


if __name__ == '__main__': # используется как отладчик для того чтобы не запускалось в других файлах
    #print(date_is_true('01.15.2024'))
    #print(date_is_true('32.11.2025'))
    #print(date_is_true('01.11.10000'))
    print(date_is_true(argv[1]))
