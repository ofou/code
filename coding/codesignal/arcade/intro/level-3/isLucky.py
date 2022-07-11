def isLucky(n):
    numbers = list(map(int, str(n)))
    return (sum(numbers[:len(numbers)//2]) == sum(numbers[len(numbers)//2:]))
