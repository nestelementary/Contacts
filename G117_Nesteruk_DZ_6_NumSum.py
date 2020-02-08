"""Создать функцию, которая прибавляет элементы числа между собой.
Например, есть число 123. Попав в нашу функцию, должно произойти следующее:
1 + 2 + 3 = 6. Результат суммирования - в консоль. """


def num_sum():
    """num_sum sums the number's digits"""
    num = (input("Input the number:\n"))
    dig_list = list(num[0:len(num)])
    dig_sum = sum(int(x) for x in dig_list)
    return dig_sum


print("The sum of the digits of your number is", num_sum(), ".")