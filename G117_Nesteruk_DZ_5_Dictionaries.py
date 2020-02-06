"""Необходимо создать три словаря и написать функцию,
которая сможет брать словари и производить их слияние в один"""


def fun_dict(x, y, z):
    """fun_dict merges three given dictionaries"""
    d = {**x, **y, **z}
    return d


d1 = dict(a=1, b=2, c=3)
d2 = dict(d=4, e=5, f=6)
d3 = dict(g=7, h=8, i=9)
print("Dictionary 1:", d1)
print("Dictionary 2:", d2)
print("Dictionary 3:", d3)
print("Combined dictionary:", fun_dict(d1, d2, d3))
