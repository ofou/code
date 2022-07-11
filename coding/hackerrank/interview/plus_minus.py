#!/bin/python3

import math
import os
import random
import re
import sys


def plusMinus(arr):
    negative = list(filter(lambda n: n < 0, arr))
    positive = list(filter(lambda n: n > 0, arr))
    zeroes = list(filter(lambda n: n == 0, arr))

    print(f'{len(positive)/len(arr):.4f}')
    print(f'{len(negative)/len(arr):.4f}')
    print(f'{len(zeroes)/len(arr):.4f}')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
