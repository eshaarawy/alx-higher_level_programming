#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_lst = [0] * len(my_list)
    for i in range(len(my_list)):
        if i == idx:
            new_lst[i] = element
        else:
            new_lst[i] = my_list[i]
    return new_lst
