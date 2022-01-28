#from typing import List


from dataclasses import dataclass
from typing import List

class Matrix:
    def __init__(self, index, row = 0, column = 0) -> None:
        self.index = index
        self.row = row
        self.column = column
        self.data: List[List[int]] = []
        lines: List[int] = []
        for i in range(0, column): lines.append(0)
        for i in range(0, row): self.data.append(list(lines))


    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def set_value(self, row, column, value):
        self.data[row][column] = value

    def set_row(self, row: int, columns: List[int]):
        self.data.append(list(columns))
        self.row = row

    def get_matrix(self) -> List[List[int]]:
        return self.data

        


    