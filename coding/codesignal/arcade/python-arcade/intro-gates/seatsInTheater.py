def seatsInTheater(nCols, nRows, col, row):
    x = abs(nRows-row)
    y = abs(nCols-col+1)
    return x*y
