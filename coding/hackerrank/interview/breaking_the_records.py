#!/bin/python3

import math
import os
import random
import re
import sys


def breakingRecords(scores):

    min_ = 0
    max_ = 0

    minimum = 0
    maximum = 0

    for i, s in enumerate(scores):
        if i == 0:
            minimum = s
            maximum = s
            continue
        if s > maximum:
            max_ += 1
            maximum = s
        if s < minimum:
            min_ += 1
            minimum = s
    return max_, min_


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
