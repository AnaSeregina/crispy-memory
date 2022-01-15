#!python3

from collections import namedtuple
from typing import List, Dict, NamedTuple


class MatrixPoint(NamedTuple):
    matrix_num: int
    row_num: int
    col_num: int


def file_read(file_name) -> List[str]:
    file_data_list: List[str] = []
    with open(file_name) as f:
        for line in f:
            file_data_list.append(line.strip())
    return file_data_list


def create_bingo_card_dictionary(dictionary: Dict, key: str, value: MatrixPoint) -> Dict:
    dict_value: List[MatrixPoint] = []
    if (key in dictionary):
        dict_value = list(dictionary[key])
        dict_value.append(value)
        dictionary[key] = dict_value
    else:
        dict_value.append(value)
        dictionary[key] = dict_value
    return dictionary


def build_empty_matrix(matrix, rows, columns) -> List[List[int]]:
    lines: List[int] = []
    for i in range(0, columns): lines.append(0)
    for i in range(0, rows): matrix.append(list(lines))
    return matrix
    

def print_result(win_matrix: int, win_number: int, final_score: int, message: str) -> None:
    print(f"{message}")
    print(f"win_matrix = {win_matrix}")
    print(f"win_number = {win_number}")
    print(f"final_score = {final_score}")
    

def check_winner(matrix_of_wins: List[List[int]], matrix: int, row: int, column: int, length: int) -> bool:
    matrix_of_wins[matrix][row] += 1
    matrix_of_wins[matrix][column] += 1
    if (matrix_of_wins[matrix][row] == length or matrix_of_wins[matrix][column] == length):
        return True
    return False


def update_winner_dictionary(win_matrix_dict: Dict[int, int], matrix: int) -> Dict[int, int]:
    if (matrix in win_matrix_dict):
        win_matrix_dict[matrix] = int(win_matrix_dict[matrix] + 1)
    else:
        win_matrix_dict[matrix] = 1
    return win_matrix_dict


def first_winner_matrix(win_matrix_dict, matrix, bingo_number, final_score) -> None:
    if (len(win_matrix_dict) == 1 and win_matrix_dict[matrix] == 1):
        print_result(matrix, int(bingo_number), final_score, "\n\nThe FIRST matrix that wins!!!")


def last_winner_matrix(win_matrix_dict, matrix, bingo_number, final_score, matrix_count) -> bool:  
    if (len(win_matrix_dict) == matrix_count):
        print_result(matrix, int(bingo_number), final_score, "\n\nThe LAST matrix that wins!!!")
        return True
    return False


def main():
    input: List[str] = file_read("day4.txt")
    if not input:
        print("Error: File is empty")
        return
    
    row_index = 0
    matrix_index = -1
    matrix_length: int = 0
    sum_of_elements: int = 0
    matrix_points_for_bingo_number: Dict[str, List[MatrixPoint]] = {}
    total_unmarked_elements_matrix: List[int] = []

    for index in range(1, len(input)):
        line = input[index]
        if not line:
            row_index = 0
            matrix_index += 1
            sum_of_elements = 0
            total_unmarked_elements_matrix.append(0)
        else:
            matrix_length = len(line.split())
            for colomn_index in range(0, matrix_length):
                item = line.split()[colomn_index]
                sum_of_elements += int(item)
                matrix_points_for_bingo_number = create_bingo_card_dictionary(matrix_points_for_bingo_number, item, MatrixPoint(matrix_index, row_index, colomn_index))
            total_unmarked_elements_matrix[matrix_index] = sum_of_elements
            row_index += 1
    matrix_count: int = matrix_index + 1
    columns: int = matrix_length * 2
    win_lines_conditon_matrix: List[List[int]] = []
    win_lines_conditon_matrix = build_empty_matrix(win_lines_conditon_matrix, matrix_count, columns)
    
    final_score: int = 0
    winner: bool = False
    win_matrix_dict: Dict[int, int] = {}
    matrix_points_list: List[MatrixPoint] = []
    bingo_balls: List[str] = input[0].split(",")
    for i in range(0, len(bingo_balls)):
        bingo_number = bingo_balls[i]
        matrix_points_list = matrix_points_for_bingo_number[bingo_number]
        for m in matrix_points_list:
            current_matrix = m.matrix_num
            row_position = m.row_num
            column_position = m.col_num  + matrix_length
            total_unmarked_elements_matrix[current_matrix] -= int(bingo_number)
            winner = check_winner(win_lines_conditon_matrix, current_matrix, row_position, column_position, matrix_length)
            if (winner):
                final_score = total_unmarked_elements_matrix[current_matrix] * int(bingo_number)
                win_matrix_dict = update_winner_dictionary(win_matrix_dict, current_matrix)
                
                first_winner_matrix(win_matrix_dict, current_matrix, int(bingo_number), final_score)
                last_matrix = last_winner_matrix(win_matrix_dict, current_matrix, int(bingo_number), final_score, matrix_count)
                if (last_matrix):
                    return


if __name__ == "__main__":
    main()