#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the rotLeft function below.
def rotLeft(a, d):
    len_of_list = len(a)

    new_list = []

    for index, value in enumerate(a):
        new_index = index - d
        if new_index < 0:
            new_index = ((len_of_list + 1) + new_index)

        new_list.insert(new_index, value)

    return new_list


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    d = 2

    result = rotLeft(a, d)

    print(result)
