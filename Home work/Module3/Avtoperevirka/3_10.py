"""
Ми проводимо розіграш призів серед перших 50 підписників ютуб-каналу.
Ми маємо 7 призів для розіграшу.
Може виникнути питання, скільки різних списків переможців ми можемо отримати під час розіграшу?
Для цього ми будемо використовувати формулу сполучень без повторень

Cnk = n! / ((n - k)! · k!)

де n — це загальна кількість людей (випадків), а k — кількість людей, які отримали призи.

Напишіть функцію number_of_groups, яка приймає параметри n та k,
і за допомогою функції factorial повертає нам скільки різних списків переможців
ми можемо отримати при розіграші

Зверніть увагу на те, які великі значення ми отримуємо для факторіала.
Рекурсивні висловлювання треба завжди застосовувати з обережністю при обчисленнях,
щоб не отримати переповнення пам'яті.

"""

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_k(k):
    if k <= 1:
        return 1
    else:
        return k * factorial_k(k - 1)


def factorial_n_k(nik):
    if nik <= 1:
        return 1
    else:
        return nik * factorial_n_k(nik - 1)


def number_of_groups(n, k):
    nik = n - k
    win = factorial(n) / (factorial_n_k(nik) * factorial_k(k))

    return int(win)



# result = factorial(50)
# print(factorial(50))
print(number_of_groups(30, 5))
# print(result)
# print(factorial_k(7))
# print(factorial_n_k(nk))
# print(number_of_groups(n))