#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    t = int(1)
    for t_itr in range(t):
        expression = list('[]([][])(){}{{}{[](){}}}()[]({})[{}')

        balance = []
        curly = ['{', '}']
        brace = ['[', ']']
        paren = ['(', ')']
        left = ['{', '[', '(']
        right = ['}', ']', ')']

        balanced_brackets = True

        for char in expression:
            if char in left:
                balance.append(char)
            elif char in right:
                if [balance.pop(), char] not in [curly, brace, paren]:
                    balanced_brackets = False

            if not balanced_brackets:
                break

        print('YES') if balanced_brackets else print('NO')




