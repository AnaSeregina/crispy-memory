#!python3

from typing import List

def file_read(file_name) -> List[int]:
    file_data_list: List[int] = []
    with open(file_name) as f:
        for line in f:
            file_data_list.append(int(line))
    return file_data_list


def main():
    data_list: List[int] = file_read("day1_1.txt")
    #data_list: List[int] = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    increases_count = 0
    for i in range(1, len(data_list)):
        if (data_list[i] > data_list[i-1]):
            increases_count += 1
    print(f"increases_count = {increases_count}")
    

if __name__ == "__main__":
    main()