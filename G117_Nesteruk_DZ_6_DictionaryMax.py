"""Найдите три ключа с самыми высокими значениями в словаре
my_dict = {'a':645, 'b':3987, 'c': 093,'d':111, 'e':646, 'f': 20}"""
my_dict = {'a': 645, 'b': 3987, 'c': 93, 'd': 111, 'e': 646, 'f': 20}
print("Your dictionary is:", my_dict)
value_list = []
key_list = []
for x in my_dict:
    value_list = value_list + [my_dict[x]]
    key_list = key_list + [x]
i = 1
while i <= 3:
    max_index = value_list.index(max(value_list))
    print('The key of the dictionary maximum value No', i, 'is', '"', key_list[max_index], '"')
    del value_list[max_index]
    del key_list[max_index]
    i = i + 1


