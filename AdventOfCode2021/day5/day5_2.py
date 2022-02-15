#!python3
from typing import Dict, List
from point import Point
from line import Line

def read_file(file_name) -> List[Line]:
    lines: List[Line] = []
    with open(file_name) as f:
        for line in f:
            point = line.strip().split(" -> ")
            start_point = list(map(int, point[0].split(",")))
            end_point = list(map(int, point[1].split(",")))
            p_start: Point = Point(start_point[0], start_point[1])
            p_end: Point = Point(end_point[0], end_point[1])
            l: Line = Line(p_start, p_end)
            lines.append(l)
    return lines


def point_overlaps(lines: List[Line]) -> Dict[Point, int]:
    point_overlaps_amount: Dict[Point, int] = {}
    for i in range(len(lines)):
        line_points: List[Point] = lines[i].get_all_points()
        for point in line_points:
            counter = 1
            if point in point_overlaps_amount:
                counter += point_overlaps_amount.get(point)
            point_overlaps_amount[point] = counter
    return point_overlaps_amount


def points_number_of_two_overlaps(lines: List[Line]) -> int:
    point_overlaps_amount: Dict[Point, int] = point_overlaps(lines)
    points_number = 0
    for overlap_number in point_overlaps_amount.values():
        if overlap_number >= 2:
            points_number += 1
    return points_number


def main():
    lines: List[Line] = read_file("AdventOfCode2021/day5/day5.txt")
    points_number: int = points_number_of_two_overlaps(lines)
    print(f"\nAt how many points do at least two lines overlap?\nPoints number: {points_number}")
    
if __name__ == "__main__":
    main()