#!python3

from typing import List

def file_read(file_name) -> List[str]:
    result: List[str] = []
    with open(file_name) as f:
        for line in f:
            result.append(line.strip())
    return result


def main():
    input: List[str] = file_read("day3_1.txt")
    max_value: List[int] = []
    for i in range(0, len(input)):
        for index in range(0, len(input[i])):
            if len(max_value) < len(input[i]):
                max_value.append(0)
            if input[i][index] == '1':
                max_value[index] += 1
            
    min_value: List[int] = []
    for i in range(0, len(max_value)):
        if (max_value[i] > (len(input) - max_value[i])):
            max_value[i] = 1
            min_value.append(0)
        else:
            max_value[i] = 0
            min_value.append(1)
 
    max_value_string = "".join([str(value) for value in max_value])
    min_value_string = "".join([str(value) for value in min_value])

    gamma_rate = int(max_value_string, 2)
    epsilon_rate = int(min_value_string, 2)
    power_consumption  = gamma_rate * epsilon_rate
    print(f"max_value = {max_value}   min_value = {min_value}")
    print(f"gamma_rate = {gamma_rate} epsilon_rate = {epsilon_rate} power_consumption = {power_consumption}")


if __name__ == "__main__":
    main()