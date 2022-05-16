list_nambers = []
shopping = []
purchase_history = {}

def product(title, price):
    balance = sum(list_nambers) - sum(shopping)
    if purchase == title:
        balance -= price
        shopping.append(price)
        purchase_history[title] = price

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. остаток на счете')
    print('5. выход')


    balance = sum(list_nambers) - sum(shopping)
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        check = 0
        namber = input('Введите сумму на сколько пополнить счет: ')
        if int(namber) > 0:
            check += int(namber)
            list_nambers.append(check)
            pass
        else:
            pass
    elif choice == '2':
        namber = int(input('Введите сумму покупки: '))
        if namber > balance:
            print('Денег не хватает.')
            pass
        else:
            purchase = input('Введите название покупки(молоко,хлеб,масло): ')
            product('молоко', 60)
            product('хлеб',40)
            product('масло', 130)
            pass
    elif choice == '3':
        print(purchase_history)
        pass
    elif choice == '4':
        print('Всего на счете: ', balance)
        pass
    elif choice == '5':
        break
    else:
        print('Неверный пункт меню')




