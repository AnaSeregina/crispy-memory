#!python3

from tracemalloc import stop
from typing import List
from xmlrpc.client import Boolean


def read_file(file_name) -> List[int]:
    numbers: List[int] = []
    with open(file_name) as f:
        for line in f:
            numbers.append(int(line.strip()))
    numbers.sort()
    return numbers


def find_and_multiply(numbers: List[int]) -> int:
    result: int = 0
    break_loop: Boolean = False
    for i in range(len(numbers)-1):
        n1 = numbers[i]
        sum_n2_n3 = 2020 - n1
        j = i + 1
        
        while (sum_n2_n3 > 2 * numbers[j]):
            n2 = numbers[j]
            n3 = sum_n2_n3 - n2
            
            if n3 in numbers:
                result = n1 * n2 * n3
                break_loop = True
                break
            j+=1
        
        if (break_loop):
            break
    return result   


def main():
    numbers: List[int] = read_file("AdventOfCode2020/day1/day1.txt")
    result: int = find_and_multiply(numbers)
    print(f"The multiplication of three entries that sum to 2020 is -> {result}")
    

if __name__ == "__main__":
    main()