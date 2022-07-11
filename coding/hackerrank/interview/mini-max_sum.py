#!/bin/python3

import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    min_ = arr[:]
    min_.remove(max(arr))
    max_ = arr[:]
    max_.remove(min(arr))

    return sum(min_), sum(max_)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
