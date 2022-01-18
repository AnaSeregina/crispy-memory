#!python3

from collections import namedtuple
from typing import List, Dict, NamedTuple


class MatrixPoint(NamedTuple):
    matrix: int
    row: int
    column: int


def file_read(file_name) -> List[str]:
    file_data_list: List[str] = []
    with open(file_name) as f:
        for line in f:
            file_data_list.append(line.strip())
    return file_data_list


def create_points(dictionary: Dict, key: str, value: MatrixPoint) -> None:
    if key not in dictionary:
        dictionary[key] = []
    dictionary[key].append(value)


def empty_grid(rows, columns) -> List[List[int]]:
    matrix: List[List[int]] = []
    lines: List[int] = []
    for i in range(0, columns): lines.append(0)
    for i in range(0, rows): matrix.append(list(lines))
    return matrix
    

def print_result(win_matrix: int, win_number: int, final_score: int, message: str) -> None:
    print(f"{message}")
    print(f"win_matrix = {win_matrix}")
    print(f"win_number = {win_number}")
    print(f"final_score = {final_score}")
    

def check_winner(game_progress: List[List[int]], matrix: int, row: int, column: int, length: int) -> bool:
    game_progress[matrix][row] += 1
    game_progress[matrix][column] += 1
    return (game_progress[matrix][row] == length or game_progress[matrix][column] == length)
    

def update_winners(winners: Dict[int, int], matrix: int) -> None:
    if (matrix in winners):
        winners[matrix] = int(winners[matrix] + 1)
    else:
        winners[matrix] = 1


def print_winners(winners: Dict[int, int], matrix: int, bingo_ball: str, final_score: int, matrix_count: int) -> None:  
    if (len(winners) == 1 and winners[matrix] == 1):
        print_result(matrix, int(bingo_ball), final_score, "\n\nThe FIRST matrix that wins!!!")
    if (len(winners) == matrix_count):
        print_result(matrix, int(bingo_ball), final_score, "\n\nThe LAST matrix that wins!!!")


def stop_the_game(matrix_dict: Dict[int, int], matrix_count: int) -> bool:  
    return (len(matrix_dict) == matrix_count)
    

def main():
    input: List[str] = file_read("day4.txt")
    if not input:
        print("Error: File is empty")
        return
    
    matrix_index = -1
    unmarked_sums: List[int] = []
    points: Dict[str, List[MatrixPoint]] = {}
    for index in range(1, len(input)):
        line = input[index]
        if (line):
            matrix_length = len(line.split())
            for colomn_index in range(0, matrix_length):
                item = line.split()[colomn_index]
                unmarked_sums[matrix_index] += int(item)
                create_points(points, item, MatrixPoint(matrix_index, row_index, colomn_index))
            row_index += 1
        else:
            matrix_index += 1
            unmarked_sums.append(0)
            row_index = 0
            
    matrix_count: int = matrix_index + 1
    columns: int = matrix_length * 2
    game_progress: List[List[int]] = empty_grid(matrix_count, columns)
    
    winners: Dict[int, int] = {}
    for bingo_ball in input[0].split(","):
        for m in points[bingo_ball]:
            unmarked_sums[m.matrix] -= int(bingo_ball)
            winner = check_winner(game_progress, m.matrix, m.row, (m.column + matrix_length), matrix_length)
            if (winner):
                update_winners(winners, m.matrix)
                final_score = unmarked_sums[m.matrix] * int(bingo_ball)
                print_winners(winners, m.matrix, int(bingo_ball), final_score, matrix_count)
                if (stop_the_game(winners, matrix_count)):
                    return
                

if __name__ == "__main__":
    main()