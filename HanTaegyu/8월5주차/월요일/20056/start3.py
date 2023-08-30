"""
    Solution code for "BaekJoon 마법사 상어와 파이어볼".

    - Problem link: https://www.acmicpc.net/problem/20056

    입력

    출력

"""
from sys import stdin as input

DIRECTIONS = [
    (-1, 0),  # 0
    (-1, 1),  # 1
    (0, 1),  # 2
    (1, 1),  # 3
    (1, 0),  # 4
    (1, -1),  # 5
    (0, -1),  # 6
    (-1, -1),  # 7
]

EVEN = {0, 2, 4, 6}
ODD = {1, 3, 5, 7}


def fire_ball_move(board, n):
    tmp_board = [[set() for _ in range(n)] for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if not board[row][col]:
                continue
            while board[row][col]:
                fireball = board[row][col].pop()
                nrow, ncol = move_fireball(fireball, n)
                tmp_board[nrow][ncol].add(fireball)
    return tmp_board


def move_fireball(fireball, n):
    row, col, speed, direction = fireball
    trow, tcol = DIRECTIONS[direction]
    nrow = (row + (trow * speed)) % n
    ncol = (col + (tcol * speed)) % n
    return nrow, ncol


def two_fire_ball(board):
    new_board = [[set() for _ in range(len(board))] for _ in range(len(board))]
    for row in range(len(board)):
        for col in range(len(board)):
            if len(board[row][col]) < 2:
                new_board[row][col] = board[row][col]
                continue

            even, odd, sum_mass, sum_speed = 0, 0, 0, 0
            count = len(board[row][col])
            while board[row][col]:
                fireball = board[row][col].pop()
                row, col, mass, speed, direction = fireball
                sum_mass += mass
                sum_speed += speed

                if direction % 2 == 0:
                    even += 1
                else:
                    odd += 1

            if not even or not odd:
                directions = EVEN
            else:
                directions = ODD

            sum_mass //= 5
            sum_speed //= count

            if sum_mass <= 0:
                continue

            for direction in directions:
                new_board[row][col].add(
                    (row, col, sum_mass, sum_speed, direction)
                )
    return new_board


def main():
    input = open('./test3.txt')
    N, fireball_count, move_count = map(int, input.readline().split())
    board = [[set() for _ in range(N)] for _ in range(N)]

    for _ in range(fireball_count):
        row, col, mass, speed, direction = map(int, input.readline().split())
        board[row - 1][col - 1].add((row - 1, col - 1, mass, speed, direction))

    for _ in range(move_count):
        board = fire_ball_move(board, N)
        board = two_fire_ball(board)

    answer_sum = 0
    for row in range(N):
        for col in range(N):
            if not board[row][col]:
                continue
            while board[row][col]:
                fireball = board[row][col].pop()
                answer_sum += fireball[2]
    print(answer_sum, end="")


if __name__ == '__main__':
    main()
