
from typing import List
from xmlrpc.client import boolean


class Line:
    def __init__(self, start_point: str, end_point: str) -> None:
        self.start_point = list(map(int, start_point.split(",")))
        self.end_point = list(map(int, end_point.split(",")))
        self.x_start = self.start_point[0]
        self.y_start = self.start_point[1]
        self.x_end = self.end_point[0]
        self.y_end = self.end_point[1]


    def horizontal(self) -> boolean:
        return (self.y_start == self.y_end)
        

    def vertical(self) -> boolean:
        return (self.x_start == self.x_end)

    
    def print_line(self):
        print(f"{self.start_point}   -> {self.end_point}")
        
