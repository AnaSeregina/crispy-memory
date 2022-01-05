#!python3

from typing import List

def file_read(file_name) -> List[int]:
    file_data_list: List[int] = []
    with open(file_name) as f:
        for line in f:
            file_data_list.append(int(line))
    return file_data_list


def main():
    data_list: List[int] = file_read("day1_2.txt")
    #data_list: List[int] = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    increases_count = 0
    sum0 = 0
    for i in range(0, len(data_list)-2):
        sum = data_list[i] + data_list[i + 1] + data_list[i + 2]
        if not (sum0 == 0):
            if (sum > sum0):
                increases_count += 1
        sum0 = sum
    print(f"increases_count = {increases_count}")
    

if __name__ == "__main__":
    main()