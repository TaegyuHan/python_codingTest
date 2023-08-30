"""
    Solution code for "BaekJoon 마법사 상어와 파이어볼".

    - Problem link: https://www.acmicpc.net/problem/20056

    입력

    출력

"""
from collections import defaultdict
from sys import stdin as input
from typing import List, Any

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


# def show_map() -> None:
#     board = [[0 for _ in range(N)] for _ in range(N)]
#     for (row, col), balls in fireballs.items():
#         board[row][col] = balls.pop()[0]
#     for row in board:
#         print(*row)

def move():
    """ 움직임 """
    tmp_balls = defaultdict(set)

    # 파이어볼 이동
    for (row, col), balls in fireballs.items():
        while balls:
            mass, speed, direction = balls.pop()
            trow, tcol = DIRECTIONS[direction]
            nrow = (row + (trow * speed)) % N
            ncol = (col + (tcol * speed)) % N
            print(nrow, ncol)
            tmp_balls[(nrow, ncol)].add((mass, speed, direction))

    # 파이어볼 2개 이상
    keys = list(tmp_balls.keys())

    for (row, col) in keys:

        balls = tmp_balls[(row, col)]

        if len(balls) < 2:
            continue

        even, odd, sum_mass, speed_sum = 0, 0, 0, 0

        for ball in balls:
            mass, speed, direction = ball
            sum_mass += mass  # 1. 질량
            speed_sum += speed  # 2. 속력

            if direction in EVEN:
                even += 1
            else:
                odd += 1

        del tmp_balls[(row, col)]

        if not odd or not even: # 전부 홀수 또는 짝수
            spread_direction = EVEN
        else:
            spread_direction = ODD

        for direction in spread_direction:
            trow, tcol = DIRECTIONS[direction]
            nrow, ncol = (row + trow) % N, (col + tcol) % N
            tmp_balls[(nrow, ncol)].add((sum_mass // 5, speed_sum // len(balls), direction))

    return tmp_balls

def count():
    """ 수 세기 """
    print(fireballs)
    answer = 0
    for value in fireballs.values():
        answer += value.pop()[0]
    print(answer)

def main():
    """ 메인함수 """
    show_map()

    for _ in range(move_count):
        fireballs = move()
        show_map()
    count()


if __name__ == '__main__':
    input = open('./test2.txt')
    N, fireball_count, move_count = map(int, input.readline().split())
    board_count = defaultdict(int)

    fireballs = defaultdict(set)
    for _ in range(fireball_count):
        row, col, mass, speed, direction = map(int, input.readline().split())
        row, col = row - 1, col - 1
        board_count[(row, col)] += 1
        fireballs[(row, col)].add((mass, speed, direction))

    main()