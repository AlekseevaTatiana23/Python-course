# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

# Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


import decimal
from datetime import date

decimal.getcontext().prec = 2
PERCENT_BONUS = decimal.Decimal(3) / decimal.Decimal(100)
CMD_DEPOSIT = '1'
CMD_WITHDRAW = '2'
CMD_EXIT = '3'
CMD_STORY = '4'

balance = 0
operations = 0



def deposit(amount: float) -> None:
    global operations
    global balance
    global PERCENT_BONUS
    COUNT_PERC = 3
    operations += 1
    balance += amount
    if operations % COUNT_PERC == 0:
        bonus_sum = balance * PERCENT_BONUS
        balance += bonus_sum
        print(f'Сумма бонуса {bonus_sum}')
    print(f'Текущий баланс {balance}')


def withdraw(amount: float) -> None:
    global operations
    global balance
    global PERCENT_BONUS
    COUNT_PERC = 3
    PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
    MIN_LIMIT = decimal.Decimal(30)
    MAX_LIMIT = decimal.Decimal(600)
    comission = amount * PERCENT
    if comission < MIN_LIMIT:
        comission = MIN_LIMIT
    elif comission > MAX_LIMIT:
        comission = MAX_LIMIT
    if comission + amount > balance:
        print('На счете недостаточно средств')
    else:
        operations += 1
        balance -= (amount + comission)
        print(f'Сумма снятия {amount}, комиссия {comission}')
    if operations % COUNT_PERC == 0:
        bonus_sum = balance * PERCENT_BONUS
        balance += bonus_sum
        print(f'Сумма бонуса {bonus_sum}')
    print(f'Текущий баланс {balance}')


def exit_bank():
    print("Будем рады видеть Вас снова!\n")
    exit()


def check_bank() -> int:
    MULTIPLICITY = 50
    while True:
        cash = int(input(f"f'Введите сумму опреации кратно {MULTIPLICITY}\n"))
        if cash % MULTIPLICITY == 0:
            return cash


def richness_tax() -> None:
    global balance
    RICHNESS_AMOUNT = 5_000_000
    PERCENT_RICHNESS = decimal.Decimal(10) / decimal.Decimal(100)
    if balance > RICHNESS_AMOUNT:
        sum_percent = balance * PERCENT_RICHNESS
        balance -= sum_percent
        print(f'Вычтен налог на богатство в размере {sum_percent}')
        print(f'Текущий баланс {balance}')


list_operation = []

while True:
    action = input(
        f'пополнить - {CMD_DEPOSIT}\n'
        f'снять - {CMD_WITHDRAW}\n'
        f'выйти - {CMD_EXIT}\n'
        f'вывести историю операций - {CMD_STORY}\n'
        f'Введите действие: '
    )
    if action == '1':
        richness_tax()
        cash = check_bank()
        deposit(cash)
        list_operation.append([str(date.today()), cash])
    elif action == '2':
        richness_tax()
        cash = check_bank()
        if cash < balance:
            withdraw(cash)
            list_operation.append([str(date.today()), -1 * cash])
        else:
            print("no money\n")
    elif action == '4':
        print(list_operation)
    elif action == '3':
        exit_bank()
