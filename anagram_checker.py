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
        except KeyError:
            diff_between_chars = occur_count
        num_of_deletions_needed += abs(diff_between_chars)

    return num_of_deletions_needed


if __name__ == '__main__':
    a = 'fcrxzwscanmligyxyvym'

    b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

    string_one = OrderedDict(sorted(Counter(a).items()))
    string_two = OrderedDict(sorted(Counter(b).items()))

    delete_these = num_del(string_one, string_two) + num_del(string_two, string_one)

    print(delete_these)
