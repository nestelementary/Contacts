"""Нужно написать функцию, которая будет считать сколько раз символ встречается в строке.
Например, в строке "Денис даёт нам классные задачки, которые помогут нам найти лучшую работу!" символ "е" встречается 3 раза.
"""


def count_symbol(string, symbol):
    """count_symbol gets the string and counts the number of the certain symbol occurrence"""
    x = string.count(symbol)
    return x


String = input("Input your sequence or string:\n")
Symbol = input("Input the symbol:\n")
result = 'The symbol "{}" occurs {} time(s) in your string.'
print(result.format(Symbol, count_symbol(String, Symbol)))






