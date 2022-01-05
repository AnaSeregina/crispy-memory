#!python3

from typing import List

def file_read(file_name) -> List[str]:
    result: List[str] = []
    with open(file_name) as f:
        for line in f:
            result.append(line)
    return result


def main():
    input: List[str] = file_read("day2_1.txt")
    position_data_list: List[str] = []
    pos_horizontal = 0
    pos_vertical = 0
    
    for i in range(0, len(input)):
        position_data_list = input[i].split(' ')
        if ('forward' in position_data_list[0]):
            pos_horizontal += int(position_data_list[1])
        elif ('down' in position_data_list[0]):
            pos_vertical += int(position_data_list[1])
        elif ('up' in position_data_list[0]):
            pos_vertical -= int(position_data_list[1])
        else:
            print("Something went wrong!")
            break
    result = pos_horizontal * pos_vertical
    print(f"result = {result}  pos_horizontal = {pos_horizontal}  pos_vertical = {pos_vertical}")
    

if __name__ == "__main__":
    main()