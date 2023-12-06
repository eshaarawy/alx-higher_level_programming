#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    val = 0
    key = None

    for i, j in a_dictionary:
        if j > val:
            key = i
            val = j
    return key
