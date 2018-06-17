#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine = magazine.split()
    for word in note.split():
        try:
            magazine.remove(word)
        except ValueError:
            print('No')
            return
    print('Yes')


if __name__ == '__main__':
    magazine = 'two times three is not four'

    note = 'two times two is four'

    checkMagazine(magazine, note)
