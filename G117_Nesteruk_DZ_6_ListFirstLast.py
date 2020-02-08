"""Создать функцию, которая:
Принимает последовательность чисел
Превращает ее в список
Выводит первый и последний элемент списка
"""


def fun_list():
    """fun_list gets the sequence, makes the list and outputs the first and the last items"""

    get_list = list(input("Input the sequence items, separated by spaces:\n").split())
    first = get_list[0]
    last = get_list[-1]
    print("Your list is:", get_list)
    return first, last


F, L = fun_list()
print("The first item of your list is", F, "and the last one is", L, ".")




