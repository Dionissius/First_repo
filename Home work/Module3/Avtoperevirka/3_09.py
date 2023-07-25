"""
Для функції попереднього завдання створіть рядки документації. Можна використовувати наступний шаблон
"""


def cost_delivery(quantity, *_, discount=0):
    """
    Функція повертає суму за доставлення замовлення.
    -----------------------------------------------
    Перший параметр quantity, кількість товарів в замовленні.
    Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0.
    """
    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result

# help(cost_delivery)
print(cost_delivery.__doc__)