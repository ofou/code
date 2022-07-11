#!/bin/python3

import math
import os
import random
import re
import sys


def timeConversion(s):
    if 'AM' in s:
        lista = s.split(":")
        if int(lista[0]) == 12:
            return ':'.join(['00', lista[1], lista[2][:-2]])
        return s[:-2]
    else:
        s = s[:-2]
        lista = s.split(":")
        hour = str(abs(int(lista[0])+12))

        if int(hour) == 24:
            return ':'.join(['12', lista[1], lista[2]])
        return ':'.join([hour, lista[1], lista[2]])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
