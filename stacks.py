#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def is_balanced(expression):
    balance = []
    curly, brace, paren = ('{', '}'), ('[', ']'), ('(', ')')

    balanced_brackets = True

    for index, char in enumerate(expression):
        try:
            if char in (curly[0], brace[0], paren[0]) and expression[index + 1]:
                balance.append(char)
            elif char in (curly[1], brace[1], paren[1]):
                if (balance.pop(), char) not in [curly, brace, paren]:
                    balanced_brackets = False

        except IndexError:
            balanced_brackets = False

    return balanced_brackets


if __name__ == '__main__':
    t = int(1)
    for t_itr in range(t):
        expression = list('[]([][])(){}{{}{[](){}}}()[]({})[{}')

        print('YES') if is_balanced(expression) else print('NO')
