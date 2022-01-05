#!python3

from typing import List

def file_read(file_name) -> List[str]:
    result: List[str] = []
    with open(file_name) as f:
        for line in f:
            result.append(line)
    return result


def main():
    input: List[str] = file_read("day2_2.txt")
    position_data_list: List[str] = []
    pos_horizontal = 0
    depth = 0
    aim = 0
    
    for i in range(0, len(input)):
        position_data_list = input[i].split(' ')
        key = position_data_list[0]
        value = int(position_data_list[1])
        if ('forward' in key):
            pos_horizontal += value
            depth += value * aim
        elif ('down' in key):
            aim += value
        elif ('up' in key):
            aim -= value
        else:
            print("Something went wrong!")
            return
    result = pos_horizontal * depth
    print(f"result = {result}  pos_horizontal = {pos_horizontal}  depth = {depth}")
    

if __name__ == "__main__":
    main()