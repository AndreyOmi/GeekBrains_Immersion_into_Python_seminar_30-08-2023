'''
Задача № 4: Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.
'''

MULTIPLICITY = 50
TAX_RATE = 0.015
TAX_MIN_LIMIT = 30
TAX_MAX_LIMIT = 600
EXPECTED_OPERATION = 3
EXPECTED_OPERATION_RATE = 0.03
WEALTH_LIMIT = 5_000_000
WEALTH_LIMIT_RATE = 0.1

operations_list = [] ### список для сохранения операций

#### Функция для пополнения счета
def deposit(balance, amount, operations_count, operations_list):
    
    if balance > WEALTH_LIMIT:
        wealth_tax = balance * WEALTH_LIMIT_RATE
        balance -= wealth_tax
        print(f"Ваш баланс превышает сумму в 5 млн, удержан налог на богатство 10%. Текущий баланс: {balance} у.е.")

    if amount % MULTIPLICITY != 0:
        print(f"Депозит должен быть пополнен на сумму, кратную 50 у.е. Пополнение не выполнено!")
        print(f"Текущий баланс: {balance} у.е.")
        return balance, operations_count, operations_list
    
    if operations_count % EXPECTED_OPERATION == 0:
        balance += amount
        balance += balance * EXPECTED_OPERATION_RATE
        print(f"Вы совершили третью операцию. Ваш баланс пополняется на {EXPECTED_OPERATION_RATE * 100} %, что составляет {balance * EXPECTED_OPERATION_RATE} у.е.")
    else:
        balance += amount
    
    operations_count += 1
    print(f"Депозит пополнен на {amount} у.е. Текущий баланс: {balance} у.е.")
    operations_list.append(f"Депозит пополнен на {amount} у.е.")
    return balance, operations_count, operations_list

#### Функция для списания средств со счета
def withdraw(balance, amount, operations_count, operations_list):
    
    if balance > WEALTH_LIMIT:
        wealth_tax = balance * WEALTH_LIMIT_RATE
        balance -= wealth_tax
        print(f"Ваш баланс превышает сумму в 5 млн, удержан налог на богатство 10%. Текущий баланс: {balance} у.е.")
    
    if amount % MULTIPLICITY != 0:
        print(f"Списание с депозита должено быть на сумму, кратную 50 у.е. Списание не выполнено!")
        print(f"Текущий баланс: {balance} у.е.")
        return balance, operations_count, operations_list
    
    if balance < amount:
        print(f"Недостаточно средств на счете. Списание не выполнено!")
        return balance, operations_count, operations_list
    
    withdrawal_fee = max(min(amount * TAX_RATE, TAX_MAX_LIMIT), TAX_MIN_LIMIT)
    print(f"Удержана комиссия в размере {withdrawal_fee} у.е.")
    balance -= amount + withdrawal_fee

    if operations_count % EXPECTED_OPERATION == 0:
        balance += balance * EXPECTED_OPERATION_RATE
        print(f"Вы совершили третью операцию. Ваш баланс пополняется на {EXPECTED_OPERATION_RATE * 100} %, что составляет {balance * EXPECTED_OPERATION_RATE} у.е.")
    
    operations_count += 1
    print(f"К выдачи {amount} у.е. Текущий баланс: {balance} у.е.")
    operations_list.append(f"Со счета списано: {amount} у.е.")
    return balance, operations_count, operations_list

### Функция проверки баланса
def check_balance(balance, operations_list):
    if balance > WEALTH_LIMIT:
        wealth_tax = balance * WEALTH_LIMIT_RATE
        balance -= wealth_tax
        print(f"Ваш баланс превышает сумму в 5 млн, удержан налог на богатство 10%. Текущий баланс: {balance} у.е.")
    print(f"Текущий баланс: {balance} у.е.")
    print(f"История поступления и снятия средств со счета: {operations_list}")

balance = 0
operations_count = 1
    
while True:
    print("\nВыберите действие:")
    print("1. Пополнение депозита")
    print("2. Списание (снятие) средств")
    print("3. Проверка баланса")
    print("4. Выход")
        
    choice = input()
        
    if choice == "1":
        print(f"Текущий баланс: {balance} у.е.")
        #print(f"Счетчик операций = {operations_count}")
        amount = int(input("Введите сумму пополнения: "))
        balance, operations_count, operations_list = deposit(balance, amount, operations_count, operations_list)
    elif choice == "2":
        print(f"Текущий баланс: {balance} у.е.")
        #print(f"Счетчик операций = {operations_count}")
        amount = int(input("Введите сумму списания: "))
        balance, operations_count, operations_list = withdraw(balance, amount, operations_count, operations_list)
    elif choice == "3":
        #print(f"Счетчик операций = {operations_count}")
        check_balance(balance, operations_list)
    elif choice == "4":
        print("Благодарим Вас за использование нашего банкомата. Ваш сеанс работы завершен.")
        exit()
    else:
        print("Введен неправильный номер действия! Пожалуйста, сделайте правильный выбор.")