"""
    Solution code for "BaekJoon 원판 돌리기".

    - Problem link: https://www.acmicpc.net/problem/17822

    입력
        - N, M, T
        - N개의 줄에 원판에 적힌 수가 주어진다. i번째 줄의 j번째 수는 (i, j)에 적힌 수
        - T개의 줄에 xi, di, ki
    출력
        원판을 T번 회전시킨 후 원판에 적힌 수의 합을 출력한다.

"""
from sys import stdin as input

# input = open('./test5.txt')

MOVE = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]


def show_board() -> None:
    for row in board:
        print(*row)
    print()


def turn(number: int, direction: int, count: int) -> None:
    move = count % number_max
    # print('turn', move)
    for index in range(number - 1, board_count, number):
        tmp = [0 for _ in range(number_max)]
        for _from in range(number_max):
            if not direction:
                to = (_from + move) % number_max
            else:
                to = (_from - move) % number_max
            tmp[to] = board[index][_from]
        board[index] = tmp


def clear() -> bool:
    """ 0으로 변경하기 """
    change = set()
    for row in range(board_count):
        for col in range(number_max):
            for trow, tcol in MOVE:
                nrow, ncol = trow + row, tcol + col
                if not (0 <= nrow < board_count): continue
                if not (-1 <= ncol < number_max): ncol = 0
                if board[nrow][ncol] == 0: continue
                if board[nrow][ncol] != board[row][col]: continue
                change.add((row, col))

    for row, col in change:
        board[row][col] = 0

    return bool(change)


def average() -> None:
    tmp_sum = 0
    count = 0
    for row in range(board_count):
        for col in range(number_max):
            if board[row][col] == 0: continue
            count += 1
            tmp_sum += board[row][col]

    if not count: return
    avg = tmp_sum / count

    # print("avg", avg, count, tmp_sum)
    for row in range(board_count):
        for col in range(number_max):
            if board[row][col] == 0: continue

            if board[row][col] < avg:
                board[row][col] += 1
            elif avg < board[row][col]:
                board[row][col] -= 1


def answer() -> None:
    answer = 0
    for row_data in board:
        answer += sum(row_data)
    print(answer, end="")


def main() -> None:
    """ 메인함수 """
    for _ in range(turn_count):
        number, direction, count = map(int, input.readline().split())
        turn(number, direction, count)
        # show_board()
        if not clear():
            average()
        # show_board()
    answer()


if __name__ == '__main__':
    board_count, number_max, turn_count = map(int, input.readline().split())
    board = [list(map(int, input.readline().split())) for _ in range(board_count)]
    main()