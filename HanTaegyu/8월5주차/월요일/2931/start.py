"""
    Solution code for "BaekJoon 가스관".

    - Problem link: https://www.acmicpc.net/problem/2931

    입력

    출력

"""
from sys import stdin as input
from typing import List, Any, Tuple

PIPE_TYPE = {
    "|": {
        (-1, 0),
        (1, 0)
    },
    "-": {
        (0, -1),
        (0, 1)
    },
    "+": {
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    },
    "1": {
        (1, 0),
        (0, 1)
    },
    "2": {
        (-1, 0),
        (0, 1)
    },
    "3": {
        (-1, 0),
        (0, -1)
    },
    "4": {
        (1, 0),
        (0, -1)
    }
}

MOVE = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

CONNECTION = {
    (1, 0): (-1, 0),
    (-1, 0): (1, 0),
    (0, 1): (0, -1),
    (0, -1): (0, 1)
}


def show_board(data: List[Any]) -> None:
    for row_data in data:
        print(*row_data)
    print()


def empty_space() -> Tuple[int, int]:
    # 파이프 수리 장소 찾기
    for row in range(ROW):
        for col in range(COL):
            if board[row][col] in ['.', "M", "Z"]:
                continue
            data = board[row][col]

            for trow, tcol in PIPE_TYPE[data]:
                nrow, ncol = row + trow, col + tcol
                if not ((0 <= nrow < ROW) and (0 <= ncol < COL)):
                    continue
                if board[nrow][ncol] != ".":
                    continue

                # print(nrow, ncol, data, board[nrow][ncol])
                return nrow, ncol


def solution() -> None:
    """ 메인함수 """
    row, col = empty_space()
    direction = set()

    for trow, tcol in MOVE:  # 파이프 연결 방향 찾기
        nrow, ncol = row + trow, col + tcol
        if not ((0 <= nrow < ROW) and (0 <= ncol < COL)):
            continue
        if board[nrow][ncol] in ['.', "M", "Z"]:
            continue

        for cnrow, cncol in PIPE_TYPE[board[nrow][ncol]]:
            if CONNECTION[(trow, tcol)] != (cnrow, cncol):
                continue
            direction.add((trow, tcol))  # 연결 가능한 방향

    for pipe_type, value in PIPE_TYPE.items():  # 가능한 파이프 찾기
        if value == direction:
            print(row + 1, col + 1, pipe_type, end="")
            break


if __name__ == '__main__':
    input = open('./test2.txt')
    ROW, COL = map(int, input.readline().split())
    board = [list(input.readline().strip()) for _ in range(ROW)]

    solution()
