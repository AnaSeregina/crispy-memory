
from typing import List, Tuple
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


    def get_all_points(self) -> List[tuple]:
        line_points: List[tuple] = []
        if (self.horizontal()):
            point0 = min(self.x_start, self.x_end)
            point1 = max(self.x_start, self.x_end)
            for i in range(point0, point1 + 1):
                line_point: tuple = (i, self.y_start)
                line_points.append(line_point)            
        elif (self.vertical()):
            point0 = min(self.y_start, self.y_end)
            point1 = max(self.y_start, self.y_end)
            for i in range(point0, point1 + 1):
                line_point: tuple = (self.x_start, i)
                line_points.append(line_point)
        else:
            print(f"Diagonal?")
        return line_points        
