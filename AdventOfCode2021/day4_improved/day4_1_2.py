#!python3

from collections import namedtuple
from typing import List, Dict, NamedTuple
from matrix import Matrix


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


def create_points(dictionary: Dict, key: int, value: MatrixPoint) -> None:
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


def sum_row(matrix: List[List[int]], row: int) -> int:
    return sum(matrix[row])


def sum_column(matrix: List[List[int]], column: int) -> int:
    return sum([row[column] for row in matrix])


def sum_unmarked(matrix: List[List[int]]) -> int:
    return sum([c for r in matrix for c in r if not (c == -1)])


def check_winner(sum_r: int, sum_c: int, length: int) -> bool:
    return (sum_r == length or sum_c == length)        


def input_chunks(input: List[str]) -> List[List[str]]:
    length_input = len(input)
    idx_list = [idx + 1 for idx, val in enumerate(input) if val == '']
    return [input[i: j] for i, j in zip([0] + idx_list, idx_list + ([length_input] if idx_list[-1] != length_input else []))]


def game(winners, grid, matrix_index, row, column, bingo_ball, matrix_count, point_replacer):
    winner = check_winner((sum_row(grid, row) * point_replacer), (sum_column(grid, column) * point_replacer), len(grid[row]))
    if (winner):
        update_winners(winners, matrix_index)
        final_score = sum_unmarked(grid) * bingo_ball
        print_winners(winners, matrix_index, bingo_ball, final_score, matrix_count)
        return (stop_the_game(winners, matrix_count))


def solution_original(input):
    matrix_index = -1
    unmarked_sums: List[int] = []
    points: Dict[int, List[MatrixPoint]] = {}
    for index in range(1, len(input)):
        line = input[index]
        if (line):
            matrix_length = len(line.split())
            for colomn_index in range(0, matrix_length):
                item = int(line.split()[colomn_index])
                unmarked_sums[matrix_index] += item
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
    balls: List[int] = list(map(int, input[0].split(",")))
    for bingo_ball in balls:
        for m in points[bingo_ball]:
            unmarked_sums[m.matrix] -= bingo_ball
            game_progress[m.matrix][m.row] += 1
            game_progress[m.matrix][m.column + matrix_length] += 1
            winner = check_winner(game_progress[m.matrix][m.row], game_progress[m.matrix][m.column + matrix_length], matrix_length)
            if (winner):
                update_winners(winners, m.matrix)
                final_score = unmarked_sums[m.matrix] * bingo_ball
                print_winners(winners, m.matrix, bingo_ball, final_score, matrix_count)
                if (stop_the_game(winners, matrix_count)):
                    return


def solution2_dictionary(input):
    grids: List[Matrix] = []
    matrix_index = -1
    points: Dict[int, List[MatrixPoint]] = {}
    for index in range(1, len(input)):
        line = input[index]
        if (line):
            items: List[int] = []
            matrix_length = len(line.split())
            for colomn_index in range(0, matrix_length):
                item = int(line.split()[colomn_index])
                items.append(item)
                create_points(points, item, MatrixPoint(m.index, row_index, colomn_index))
            m.set_row(row_index, items)
            row_index += 1
        else:
            matrix_index += 1
            row_index = 0
            m = Matrix(matrix_index)
            grids.append(m)

    point_replacer: int = -1
    matrix_count: int = len(grids)
    winners: Dict[int, int] = {}
    balls: List[int] = list(map(int, input[0].split(",")))
    for bingo_ball in balls:
        for p in points[bingo_ball]:
            grids[p.matrix].set_value(p.row, p.column, point_replacer)
            grid = grids[p.matrix].get_matrix()
            if (game(winners, grid, p.matrix, p.row, p.column, bingo_ball, matrix_count, point_replacer)):
                return


def solution2_1_dictionary(input):
    chunks: List[List[str]] = input_chunks(input)
    points: Dict[int, List[MatrixPoint]] = {}
    grids: List[Matrix] = []
    for i in range(1, len(chunks)):
        chunks[i] = list(filter(None, chunks[i]))
        m = Matrix(i-1)
        grids.append(m)
        for j in range(0, len(chunks[i])):
            m_row = list(map(int, str(chunks[i][j]).split()))
            m.set_row(j, m_row)
            [create_points(points, item, MatrixPoint(m.index, j, colomn_index)) for colomn_index, item in enumerate(m_row)]
    
    point_replacer: int = -1
    matrix_count: int = len(grids)
    winners: Dict[int, int] = {}
    balls: List[int] = list(map(int, input[0].split(",")))
    for bingo_ball in balls:
        for p in points[bingo_ball]:
            grids[p.matrix].set_value(p.row, p.column, point_replacer)
            grid = grids[p.matrix].get_matrix()
            if (game(winners, grid, p.matrix, p.row, p.column, bingo_ball, matrix_count, point_replacer)):
                return


def solution3(input):
    chunks: List[List[str]] = input_chunks(input)
    grids: List[Matrix] = []
    for i in range(1, len(chunks)):
        chunks[i] = list(filter(None, chunks[i])) 
        m = Matrix(i-1)
        grids.append(m)
        for j in range(0, len(chunks[i])):
            m_row = list(map(int, str(chunks[i][j]).split()))
            m.set_row(j, m_row)
            
    point_replacer: int = -1
    matrix_count: int = len(grids)
    winners: Dict[int, int] = {}
    balls: List[int] = list(map(int, input[0].split(",")))
    for bingo_ball in balls:
        for i in range(0, len(grids)):
            grid = grids[i].get_matrix()
            for row in range(0, len(grid)):
                if (bingo_ball in grid[row]):
                    column = grid[row].index(bingo_ball)
                    grids[i].set_value(row, column, point_replacer)
                    if (game(winners, grid, grids[i].index, row, column, bingo_ball, matrix_count, point_replacer)):
                        return


def main():
    input: List[str] = file_read("day4.txt")
    if not input:
        print("Error: File is empty")
        return
    
    print(f"\n\n___Solution_original (no list of matrix, but with extra \"game_progress\" matrix)_______")
    solution_original(input)
    
    print(f"\n\n___Solution2_dictionary (list of matrix + numbers replacing; check row,column for winner)______")
    solution2_dictionary(input)

    print(f"\n\n___Solution2_1_dictionary (new parsing)__________")
    solution2_1_dictionary(input)

    print(f"\n\n___Solution3 (no dictionary)_______________")
    solution3(input)
    
                

if __name__ == "__main__":
    main()