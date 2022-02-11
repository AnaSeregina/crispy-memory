#!python3

from line import Line
from typing import List, Tuple


def file_read(file_name) -> List[Line]:
    lines: List[Line] = []
    with open(file_name) as f:
        for line in f:
            points = line.strip().split(" -> ")
            
            l: Line = Line(points[0], points[1])
            if (l.horizontal() or l.vertical()):
                lines.append(l)
    return lines


def main():
    lines: List[Line] = file_read("day5_test.txt")
    print(f"len = {len(lines)}")
    

if __name__ == "__main__":
    main()