#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    lst = [0] * list_length
    while i < list_length:
        try:
            lst[i] = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out or range")
        finally:
            i += 1
    return lst
