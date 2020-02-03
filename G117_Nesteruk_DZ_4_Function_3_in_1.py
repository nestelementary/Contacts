print('Task 1 of 3: Function "Create your list"')


def fun_list():
    """fun_list makes the list of the length = n and of the item maximum value = m"""

    n = int(input("Input the number of items in your list:\n"))
    m = int(input("Input the maximum value of the item in your list:\n"))
    q = input("Do you want to set the values of the list items by yourself? (Y/N)\n")
    your_list = list(range(m - n, m))
    i = 0
    if q == 'Y' or q == 'y':
        while i < n:
            print("Input the value of item", i + 1, "not greater than maximum value:")
            your_list[i] = int(input())
            if your_list[i] <= m:
                i = i + 1
    else:
        import random
        while i < n:
            your_list[i] = random.randint(0, m)
            i = i + 1
    print("Your list:", your_list)
    return your_list


L = fun_list()

print('\nTask 2 of 3: Function "Items greater than a given number"')


def fun_greater(your_list):
    """fun_greater creates new list from items that are greater than a given number"""
    lim = int(input("Input the lower limit (will not be included) of your new list item value (for example, 7):\n"))
    new_list = []
    for x in your_list:
        if x > lim:
            new_list[len(new_list):] = [x]
    print("Your new list:", new_list)
    return new_list


q = input("Do you want to use the list from the previous task? (Y/N)\n")
if q == 'Y' or q == 'y':
    New_L = fun_greater(L)
else:
    New_L = fun_greater(fun_list())

print('\nTask 3 of 3: Function "The list of the common items of two other lists"')


def fun_intersect(your_list_1, your_list_2):
    """fun_intersect creates a list of common items of two other lists"""
    intersect_list = []
    for x in your_list_1:
        for y in your_list_2:
            z = y in intersect_list
            if x == y and not z:
                intersect_list[len(intersect_list):] = [y]
    print("The list of the common items:", intersect_list)
    return intersect_list


q = input("Do you want to use lists from the Task 1 and the Task 2? (Y/N)\n")
if q == 'Y' or q == 'y':
    print("Your first list:", L)
    print("Your second list:", New_L)
    I_L = fun_intersect(L, New_L)
else:
    print("Let's create the first list:")
    L1 = fun_list()
    print("\nLet's create the second list:")
    L2 = fun_list()
    print("\nYour first list:", L1)
    print("Your second list:", L2)
    I_L = fun_intersect(L1, L2)