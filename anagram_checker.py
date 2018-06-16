#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, OrderedDict


def num_del(first_string, second_string):
    num_of_deletions_needed = 0

    for character, occur_count in first_string.items():
        try:
            diff_between_chars = occur_count - second_string[character]
            second_string[character] = occur_count
        except KeyError:
            diff_between_chars = occur_count

        num_of_deletions_needed += abs(diff_between_chars)

    return num_of_deletions_needed, second_string


if __name__ == '__main__':
    a = 'fcrxzwscanmligyxyvym'

    b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

    string_one = Counter(a)
    string_two = Counter(b)

    delete_these, string_two = num_del(string_one, string_two)
    delete_that, _ = num_del(string_two, string_one)

    print(delete_these + delete_that)
