import datetime


def add(a, b):
    return a + b


def mult(a, b):
    return round(a * b, 12)


def sub(a, b):
    return round(a - b, 12)


def div(a, b):
    if b == 0:
        return "Делить на ноль нельзя"
    return round(a / b, 12)


def calc():
    try:
        a = float(input("Введите число: "))
        b = float(input("Введите число: "))

    except ValueError as e:
        date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print(f"Ошибка произошла {date}[ValueError] - [{e}]: нужно ввести число")
        return

    if a is None or b is None:
        print("Некорректные значения")
        return

    oper = input("Выберите действие: +, -, *, / ").strip()

    if oper == "+":
        print(f'Результат: {add(a, b)}')

    elif oper == "-":
        print(f'Результат: {sub(a, b)}')

    elif oper == "*":
        print(f'Результат: {mult(a, b)}')

    elif oper == "/":
        print(f'Результат: {div(a, b)}')
    else:
        print("Действие не поддерживается")
        return


def run():
    c = ['C', 'c', 'С', 'с']
    while True:
        calc()
        exit = input('Продолжить вычисления - C ')
        if exit not in c:
            break


if __name__ == '__main__':
    run()
