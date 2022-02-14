#!python3

from line import Line
from typing import Dict, List, Tuple
import os


def file_read(file_name) -> List[Line]:
    lines: List[Line] = []
    with open(file_name) as f:
        for line in f:
            points = line.strip().split(" -> ")
            l: Line = Line(points[0], points[1])
            if (l.horizontal() or l.vertical()):
                lines.append(l)
    return lines


def points_number_of_two_overlaps(lines: List[Line]) -> int:
    point_overlaps_number: Dict[tuple, int] = {}
    for i in range(len(lines)):
        line_points: List[tuple] = lines[i].get_all_points()
        for point in line_points:
            counter = 1
            if point in point_overlaps_number:
                counter += point_overlaps_number.get(point)
            point_overlaps_number[point] = counter

    points_number = 0
    for overlap_number in point_overlaps_number.values():
        if overlap_number >= 2:
            points_number += 1
    return points_number


def main():
    lines: List[Line] = file_read("AdventOfCode2021/day5/day5.txt")
    points_number: int = points_number_of_two_overlaps(lines)
    print(f"At how many points do at least two lines overlap?\nPoints number: {points_number}")
    

if __name__ == "__main__":
    main()