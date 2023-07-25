"""
Наступне завдання буде суто теоретичним, і ми потренуємося працювати з довільною кількістю аргументів.

Створіть дві функції:

перша first буде мати першим параметром змінну size,
а також вона може приймати будь-яку кількість позиційних аргументів.
Функція повинна повернути суму size із загальною кількістю переданих до неї позиційних аргументів.

друга функція second так само матиме першим параметром size
і прийматиме довільну кількість ключових аргументів,
і також має повернути суму size з кількістю переданих у функцію ключових аргументів.

"""


def first(size, *args):
    size += len(args)
    print(size)
    return size

first(2, 5, 7, 5, 10, 35, 4)
first(5, "first", "second", "third")
first(1, "Alex", "Boris")

def second(size, **kwargs):
    size += len(kwargs)
    print(size)
    return size

second(3, comment_one="first", comment_two="second", comment_third="third")
second(10, comment_one="Alex", comment_two="Boris")