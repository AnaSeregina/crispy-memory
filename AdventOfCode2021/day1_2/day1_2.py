#!python3

from typing import List

def file_read(file_name) -> List[int]:
    result: List[int] = []
    with open(file_name) as f:
        for line in f:
            result.append(int(line))
    return result


def main():
    input: List[int] = file_read("day1_2.txt")
    increases_count = 0
    previous_sum = 0
    for i in range(0, len(input)-2):
        current_sum = input[i] + input[i + 1] + input[i + 2]
        if not (previous_sum == 0):
            if (current_sum > previous_sum):
                increases_count += 1
        previous_sum = current_sum
    print(f"increases_count = {increases_count}")
    

if __name__ == "__main__":
    main()