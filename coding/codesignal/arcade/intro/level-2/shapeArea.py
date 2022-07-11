def shapeArea(n):
    area = 2*n-1
    for j in range(1, 2*n-1, 2):
        area = area+2*j
    return area
