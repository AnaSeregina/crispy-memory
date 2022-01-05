#!python3

from typing import List

def file_read(file_name) -> List[int]:
    result: List[int] = []
    with open(file_name) as f:
        for line in f:
            result.append(int(line))
    return result


def main():
    input: List[int] = file_read("day1_1.txt")
    increases_count = 0
    for i in range(1, len(input)):
        if (input[i] > input[i-1]):
            increases_count += 1
    print(f"increases_count = {increases_count}")
    

if __name__ == "__main__":
    main()