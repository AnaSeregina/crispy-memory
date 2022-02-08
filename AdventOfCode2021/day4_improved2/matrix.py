#from typing import List


from dataclasses import dataclass
from typing import List
from xmlrpc.client import boolean

class Matrix:
    def __init__(self, row_num = 0, column_num = 0) -> None:
        self.row_num = row_num
        self.column_num = column_num
        self.data: List[List[int]] = []
                
        
    def add_row(self) -> int:
        self.data.append([])
        self.row_num = len(self.data) # - 1
        return (self.row_num - 1)
        

    def add_value(self, row: int, value: int):
        self.data[row].append(value)
        self.column_num = len(self.data[row]) # - 1


    def get_value(self, row: int, column: int) -> int:
        return self.data[row][column]


    def search(self, value: int) -> List[int]:
        position: List[int] = []
        for i in range(len(self.data)):
            if value in self.data[i]:
                position = [i, self.data[i].index(value)]
                break
        return position


    def set_value(self, row: int, column: int, value: int):
        self.data[row][column] = value
        
          
    def sum_row(self, row: int) -> int:
        return sum(self.data[row])


    def sum_column(self, column: int) -> int:
        return sum([row[column] for row in self.data])


    def unmarked_sum(self) -> int:
        m_sum: int = 0
        for i in range(self.row_num):
            for j in range(self.column_num):
                if self.data[i][j] != -1:
                    m_sum += self.data[i][j]
        return m_sum


    def total_sum(self) -> int:
        m_sum: int = 0
        for i in range(self.row_num):
            for j in range(self.column_num):
                m_sum += self.data[i][j]
        return m_sum    

    def print_matrix(self):
        for i in range(self.row_num):
            line: List[int] = []
            for j in range(self.column_num):
                line.append(self.data[i][j])
            print(f"{line}")
