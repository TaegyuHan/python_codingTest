"""
    Solution code for "BaekJoon 마법사 상어와 파이어볼".

    - Problem link: https://www.acmicpc.net/problem/20056

    입력

    출력

"""
from sys import stdin as input
from typing import Tuple

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


class FireBall:

    def __init__(self, row: int, col: int, mass: int, speed: int, direction: int) -> None:
        self._row = row
        self._col = col
        self._mass = mass
        self._speed = speed
        self._direction = direction

    def __repr__(self):
        # return f"FireBall({self._row}, {self._col}, {self._mass}, {self._speed}, {self._direction})"
        return f"{self._mass}"

    def get_position(self) -> Tuple[int, int]:
        return self._row, self._col

    def get_info(self) -> Tuple[int, int]:
        return self._row, self._col, self._mass, self._speed, self._direction

    def get_mass(self) -> int:
        return self._mass

    def move(self, n: int) -> Tuple[int, int]:
        trow, tcol = DIRECTIONS[self._direction]
        self._row = (self._row + (trow * self._speed)) % n
        self._col = (self._col + (tcol * self._speed)) % n
        return self._row, self._col


class Board:

    def __init__(self, n: int, count: int, move: int):
        self._n = n
        self._fire_ball_count = count
        self._move = move
        self._board = [[set() for _ in range(self._n)] for _ in range(self._n)]
        self._fire_balls = set()

    def show_board(self) -> None:
        for row in self._board:
            print(*row)
        print("\n\n")

    def set_fire_ball(self, fire_ball: FireBall) -> None:
        row, col = fire_ball.get_position()
        self._board[row][col].add(fire_ball)
        self._fire_balls.add(fire_ball)

    def move(self) -> None:
        """ 이동하기 """
        for _ in range(self._move):
            # self.show_board()
            self._fire_ball_move()  # 파이어볼 이동하기
            self._two_fire_ball()  # 두 개 이상의 파이어볼
            # self.show_board()

    def answer(self) -> None:
        answer_sum = 0
        for row in range(self._n):
            for col in range(self._n):
                if not self._board[row][col]: continue

                while self._board[row][col]:
                    fire_ball = self._board[row][col].pop()
                    answer_sum += fire_ball.get_mass()
        print(answer_sum, end="")

    def _fire_ball_move(self) -> None:
        """ 파이어볼 이동하기 """
        tmp_board = [[set() for _ in range(self._n)] for _ in range(self._n)]
        for row in range(self._n):
            for col in range(self._n):
                if not self._board[row][col]: continue
                while self._board[row][col]:
                    fireball = self._board[row][col].pop()
                    nrow, ncol = fireball.move(n=self._n)
                    tmp_board[nrow][ncol].add(fireball)
        self._board = tmp_board

    def _two_fire_ball(self) -> None:
        """ 두 개 이상의 파이어볼 """
        # self.show_board()
        for row in range(self._n):
            for col in range(self._n):
                if len(self._board[row][col]) < 2:
                    continue

                count = len(self._board[row][col])
                even, odd, sum_mass, sum_speed = 0, 0, 0, 0
                while self._board[row][col]:
                    fireball = self._board[row][col].pop()
                    row, col, mass, speed, direction = fireball.get_info()
                    sum_mass += mass
                    sum_speed += speed

                    if direction % 2 == 0:
                        even += 1
                    else:
                        odd += 1

                if not even or not odd:  # 모두 홀수 또는 모두 짝수
                    directions = EVEN
                else:
                    directions = ODD

                sum_mass //= 5
                sum_speed //= count

                if sum_mass <= 0:
                    continue

                for direction in directions:
                    self._board[row][col].add(
                        FireBall(row=row, col=col, mass=sum_mass, speed=sum_speed, direction=direction)
                    )


if __name__ == '__main__':
    input = open('./test3.txt')
    N, fireball_count, move_count = map(int, input.readline().split())
    board = Board(n=N, count=fireball_count, move=move_count)

    for _ in range(fireball_count):
        row, col, mass, speed, direction = map(int, input.readline().split())
        board.set_fire_ball(
            FireBall(row=row - 1, col=col - 1, mass=mass, speed=speed, direction=direction)
        )

    board.move()
    board.answer()