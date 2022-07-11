class Matrix:
    def __init__(self, matrix_string):
        self.data = [x.split(" ") for x in matrix_string.split("\n")]
        print(self.data)

    def row(self, index):
        return [int(x) for x in self.data[index-1]]

    def column(self, index):
        return [[int(y) for y in row if row.index(y) == index-1][0] for row in self.data]
