"""
Онлайн-магазин "У Бобра" надає послугу експрес доставлення своїх товарів
за ціною 5¤ за перший товар у замовленні та 2¤ - за всі наступні товари.
Необхідно реалізувати функцію, яка приймає як перший параметр кількість товарів у замовленні quantity,
але також має бути присутнім параметр, що передається тільки за ключем discount.

Параметр discount за замовчуванням має значення 0 - знижки немає.
Приймає значення від 0 до 1.
Функція cost_delivery повертає загальну суму за доставлення товару з урахуванням знижки.

Треба передбачити, що функція cost_delivery при визові може приймати будь-яку кількість
позиційних аргументів.

Приклад:

cost_delivery(2, 1, 2, 3)
При такому виклику quantity дорівнює 2, а параметр discount за умовчанням має значення 0.

"""

def cost_delivery(quantity, *args, discount=0):
    first = 5
    other = 2
    result = 0
    result_sale = 0

    if discount == 0:

        if quantity > 1:
            result = first + (quantity - 1) * other
            print(result)
            return result
        else:
            result = first
            print(result)
            return result

    if discount > 0:

        if quantity > 1:
            result = first + (quantity - 1) * other
            result_sale = result - (result * discount)
            print(result)
            print(result_sale)
            return result_sale
        else:
            result = first
            result_sale = result - (result * discount)
            print(result)
            print(result_sale)
            return result_sale


    print(f'Total prise is {result}')
    print(f'Prise with sale is  {result_sale}')




# cost_delivery(2, 1, 2, 3)
# cost_delivery(3,3)
# cost_delivery(1)
# cost_delivery(2, 1, 2, 3, discount=0.5)
cost_delivery(3)
