def matrixElementsSum(matrix):
    sum = 0
    ghost = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 0: 
                ghost.append(j)
            if(j in ghost):
                continue
            sum += value
    return sum