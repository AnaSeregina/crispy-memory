#!python3

from collections import namedtuple
from typing import List, Dict, NamedTuple, Tuple
from xmlrpc.client import boolean
from matrix import Matrix
from copy import deepcopy


class MatrixPoint(NamedTuple):
    matrix: int
    row: int
    column: int


def file_read2(file_name) -> Tuple:
    balls: List[int] = []
    matrices: List[Matrix] = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            if not (line):
                m: Matrix = Matrix()
                matrices.append(m)
            if (line):
                if (balls == []):
                    balls = list(map(int, line.split(",")))
                else:
                    try:
                        row: int = m.add_row()
                        for value in line.split():
                            m.add_value(row, int(value))
                    except NameError:
                        pass
    return (balls, matrices)


def print_result(win_matrix: int, win_number: int, final_score: int, message: str) -> None:
    print(f"{message}")
    print(f"win_matrix = {win_matrix}")
    print(f"win_number = {win_number}")
    print(f"final_score = {final_score}")
    

def print_winners(winners: Dict[int, int], matrix: int, bingo_ball: str, final_score: int, matrix_count: int) -> None:  
    if (len(winners) == 1 and winners[matrix] == 1):
        print_result(matrix, int(bingo_ball), final_score, "\n\nThe FIRST matrix that wins!!!")
    if (len(winners) == matrix_count):
        print_result(matrix, int(bingo_ball), final_score, "\n\nThe LAST matrix that wins!!!")


def stop_the_game(matrix_dict: Dict[int, int], matrix_count: int) -> bool:  
    return (len(matrix_dict) == matrix_count)


def sum_row(matrix: List[List[int]], row: int) -> int:
    return sum(matrix[row])


def sum_column(matrix: List[List[int]], column: int) -> int:
    return sum([row[column] for row in matrix])


def update_winner_board(winner_board: Dict[int, int], matrix: int) -> None:
    if (matrix in winner_board):
        winner_board[matrix] = int(winner_board[matrix] + 1)
    else:
        winner_board[matrix] = 1


def mark_position(m: Matrix, row: int, column: int) -> None:
    m.set_value(row, column, -1)


def line_complete(m: Matrix, row: int, column: int) -> boolean:
    return (m.sum_row(row) == -m.row_num or m.sum_column(column) == -m.column_num)


def winner_found(winner_board, matrix_index: int, bingo_ball, matrices_total, final_score) -> boolean:
    update_winner_board(winner_board, matrix_index)
    game_over = stop_the_game(winner_board, matrices_total)
    print_winners(winner_board, matrix_index, bingo_ball, final_score, matrices_total)
    return game_over


def set_dictionary(dictionary: Dict, m: Matrix, matrix_index) -> None:
    for row in range(m.row_num):
        for colm in range(m.column_num):
            key = m.data[row][colm]
            if key not in dictionary:
                dictionary[key] = []
            value: MatrixPoint = MatrixPoint(matrix_index, row, colm)
            dictionary[key].append(value)
        

def set_empty_matrix(row_num, column_num) -> Matrix:
    matrix: Matrix = Matrix()
    for i in range(row_num):
        row: int = matrix.add_row()
        for j in range(column_num):
            matrix.add_value(row, 0)
    return matrix


def set_results_matrix(m: Matrix, row: int, column1: int, column2: int):
    m.set_value(row, column1, (m.get_value(row, column1) + 1))
    m.set_value(row, column2, (m.get_value(row, column2) + 1))
    

def results_matrix_complete(m: Matrix, row: int, column1: int, column2: int, size: int) -> boolean:
    return (m.get_value(row, column1) == size or m.get_value(row, column2) == size)
          

def solution_original(input: Tuple) -> None:
    balls: List[int] = input[0]
    matrices: List[Matrix] = input[1]
    winner_board: Dict[int, int] = {}
    matrices_total: int = len(matrices)
    matrix_size = matrices[0].row_num

    points: Dict[int, List[MatrixPoint]] = {}
    unmarked_sums: List[int] = []
    for i in range(matrices_total):
        m: Matrix = matrices[i]
        set_dictionary(points, m, i)
        unmarked_sums.append(m.total_sum())

    res_rows_total = matrices_total
    res_columns_total = matrices[0].column_num + matrix_size
    results_matrix: Matrix = set_empty_matrix(res_rows_total, res_columns_total)

    
    for bingo_ball in balls:
        for p in points[bingo_ball]:

            row: int = p.row
            column: int = p.column
            m_index: int = p.matrix
            unmarked_sums[m_index] -= bingo_ball

            res_row = m_index
            res_column1 = row
            res_column2 = column + matrix_size
            set_results_matrix(results_matrix, res_row, res_column1, res_column2)

            final_score = unmarked_sums[m_index] * bingo_ball
            is_line_complete = results_matrix_complete(results_matrix, res_row, res_column1, res_column2, matrix_size)
            
            if (is_line_complete):
                game_over = winner_found(winner_board, m_index, bingo_ball, matrices_total, final_score)
                if (game_over):
                    return


def solution2_dictionary(input: Tuple) -> None:
    balls: List[int] = input[0]
    matrices: List[Matrix] = input[1]
    winner_board: Dict[int, int] = {}
    matrices_total: int = len(matrices)
    points: Dict[int, List[MatrixPoint]] = {}
    
    for i in range(matrices_total):
        m: Matrix = matrices[i]
        set_dictionary(points, m, i)

    for bingo_ball in balls:
        for p in points[bingo_ball]:
            row: int = p.row
            column: int = p.column
            m_index: int = p.matrix
            m: Matrix = matrices[m_index]

            mark_position(m, row, column)
            final_score = m.unmarked_sum() * bingo_ball
            is_line_complete = line_complete(m, row, column)
            if (is_line_complete):
                game_over = winner_found(winner_board, m_index, bingo_ball, matrices_total, final_score)
                if (game_over):
                    return


def solution3(input: Tuple) -> None:
    balls: List[int] = input[0]
    matrices: List[Matrix] = input[1]
    winner_board: Dict[int, int] = {}
    matrices_total: int = len(matrices)

    for bingo_ball in balls:
        for m_index in range(matrices_total):
            m: Matrix = matrices[m_index]
            position: List[int] = m.search(bingo_ball)
            if (position != []):
                row: int = position[0]
                column: int = position[1]

                mark_position(m, row, column)
                final_score = m.unmarked_sum() * bingo_ball
                is_line_complete = line_complete(m, row, column)
                if (is_line_complete):
                    game_over = winner_found(winner_board, m_index, bingo_ball, matrices_total, final_score)
                    if (game_over):
                        return
         

def main():
    input: Tuple = file_read2("day4.txt")
    if not input:
        print("Error: File is empty")
        return
    
    
    print(f"\n\n___Solution_original (no list of matrix, but with extra \"game_progress\" matrix)_______")
    solution_original(deepcopy(input))
    
    print(f"\n\n___Solution2_dictionary (list of matrix + numbers replacing; check row,column for winner)______")
    solution2_dictionary(deepcopy(input))

    print(f"\n\n___Solution3 (no dictionary)_______________")
    solution3(deepcopy(input))
    
                

if __name__ == "__main__":
    main()