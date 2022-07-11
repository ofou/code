def maxMultiple(divisor, bound):
    result = 0
    for N in range(1, bound+1):
        if N % divisor == 0:
            result = N
    return result
