#!python3

from typing import List


def read_file(file_name) -> List[int]:
    numbers: List[int] = []
    with open(file_name) as f:
        for line in f:
            numbers.append(int(line.strip()))
    return numbers
            

def find_and_multiply(numbers: List[int]) -> int:
    result: int = 0
    for i in range(len(numbers)):
        pair: int = 2020 - numbers[i]
        if pair in numbers:
            result = pair * numbers[i]
            break
    return result
    
    
def main():
    numbers: List[int] = read_file("AdventOfCode2020/day1/day1.txt")
    result: int = find_and_multiply(numbers)
    print(f"The multiplication of two entries that sum to 2020 is -> {result}")


if __name__ == "__main__":
    main()