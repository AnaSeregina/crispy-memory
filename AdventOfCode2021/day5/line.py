
from typing import List, Tuple
from xmlrpc.client import boolean
from point import Point


class Line:
    def __init__(self, start_point: Point, end_point: Point) -> None:
        self.start = start_point
        self.end = end_point


    def horizontal(self) -> boolean:
        return (self.start.y == self.end.y)
        

    def vertical(self) -> boolean:
        return (self.start.x == self.end.x)


    def range_params(self, start_point: int, end_point: int) -> List[int]:
        r: List[int] = [start_point, end_point+1, 1]
        if start_point > end_point:
            r = [start_point, end_point-1, -1]
        return r


    def coordinate_list(self, start_point: int, end_point: int) -> List[int]:
        param: List[int] = self.range_params(start_point, end_point)
        xy_list: List[int] = []
        for x in range(param[0], param[1], param[2]):
            xy_list.append(x)
        return xy_list


    def get_all_points(self) -> List[Point]:       
        x_list: List[int] = self.coordinate_list(self.start.x, self.end.x)
        y_list: List[int] = self.coordinate_list(self.start.y, self.end.y)
        line_points: List[Point] = []
        for i in range(max(len(x_list), len(y_list))):
            if i < len(x_list): x: int = x_list[i]
            if i < len(y_list): y: int = y_list[i]
            line_points.append(Point(x, y))
        return line_points        
