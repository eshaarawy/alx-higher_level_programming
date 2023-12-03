#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    lst = my_list.copy()
    for i in my_list:
        if i % 2 == 0:
            lst[i] = True
        else:
            lst[i] = False
    return lst
