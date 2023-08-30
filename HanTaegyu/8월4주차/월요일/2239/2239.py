"""
    Solution code for "BaekJoon 수도쿠"

    - Problem link: https://www.acmicpc.net/problem/2239
"""
import sys
from sys import stdin as input


def can_place(row: int, col: int, num: int) -> bool:
    return num not in row_check[row] \
           and num not in col_check[col] \
           and num not in box_check[row // 3][col // 3]


def place_number(row: int, col: int, num: int) -> None:
    board[row][col] = num
    row_check[row].add(num)
    col_check[col].add(num)
    box_check[row // 3][col // 3].add(num)


def remove_number(row, col, num) -> None:
    board[row][col] = 0
    row_check[row].remove(num)
    col_check[col].remove(num)
    box_check[row // 3][col // 3].remove(num)


def solve_sudoku(index: int) -> None:

    if index == len(empty_list):
        for row in board:
            print("".join(map(str, row)))
        sys.exit()

    row, col = empty_list[index]

    for num in range(1, 10):
        if can_place(row, col, num):
            place_number(row, col, num)
            solve_sudoku(index + 1)
            remove_number(row, col, num)


if __name__ == '__main__':
    input = open('test1.txt')

    board = []
    empty_list = []
    row_check = [set() for _ in range(9)]
    col_check = [set() for _ in range(9)]
    box_check = [[set() for _ in range(3)] for _ in range(3)]

    for row in range(9):
        row_data = list(map(int, input.readline().strip()))
        board.append(row_data)
        for col in range(9):
            if row_data[col] == 0:
                empty_list.append((row, col))
            else:
                num = row_data[col]
                row_check[row].add(num)
                col_check[col].add(num)
                box_check[row // 3][col // 3].add(num)

    print(empty_list)
    solve_sudoku(index=0)