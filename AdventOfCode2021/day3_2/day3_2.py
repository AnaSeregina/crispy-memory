#!python3

from typing import List

def file_read(file_name) -> List[str]:
    file_data_list: List[str] = []
    with open(file_name) as f:
        for line in f:
            file_data_list.append(line.strip())
    return file_data_list


def list_to_string(list_value: List[str]) -> str:
    return ("".join(list_value))


def list_of_binary_to_decimal(value: List[str]) -> int:
    return int(list_to_string(value), 2)


def most_common(bit0_numbers: List[str], bit1_numbers: List[str]) -> List[str]:
    if (len(bit1_numbers) >= len(bit0_numbers)):
        return bit1_numbers
    else:
        return bit0_numbers
    
    
def least_common(bit0_numbers: List[str], bit1_numbers: List[str]) -> List[str]:
    if (len(bit1_numbers) >= len(bit0_numbers)):
        return bit0_numbers
    else:
        return bit1_numbers
    

def rating_value(data_list_original: List[str], fun) -> int:
    data_list: List[str] = data_list_original
    index_n_max = len(data_list_original[0]) - 1
    index_n = 0

    while (len(data_list) > 1):
        bit0_numbers: List[str] = []
        bit1_numbers: List[str] = []
        for i in range(0, len(data_list)):
            if data_list[i][index_n] == '1':
                bit1_numbers.append(data_list[i])
            elif data_list[i][index_n] == '0':
                bit0_numbers.append(data_list[i])
        data_list = fun(bit0_numbers, bit1_numbers)
        index_n += 1
        if (index_n > index_n_max): 
            break   
    
    rating_integer_value: int = list_of_binary_to_decimal(data_list)
    return rating_integer_value


def main():
    data_list_original: List[str] = file_read("day3_2.txt")
    oxygen_generator_rating: int = 0
    co2_scrubber_rating: int = 0
    oxygen_generator_rating = rating_value(data_list_original, most_common)
    co2_scrubber_rating = rating_value(data_list_original, least_common)
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating

    print(f"oxygen_generator_rating = {oxygen_generator_rating}")
    print(f"CO2_scrubber_rating = {co2_scrubber_rating}")
    print(f"life_support_rating = {life_support_rating}")



if __name__ == "__main__":
    main()