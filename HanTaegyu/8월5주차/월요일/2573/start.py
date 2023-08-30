"""
    Solution code for "BaekJoon 빙산".

    - Problem link: https://www.acmicpc.net/problem/2573

    입력

    출력

"""
from sys import stdin as input

# 이동하기
MOVES = [
    (-1, 0),  # 아래
    (1, 0),   # 위
    (0, -1),  # 왼쪽
    (0, 1),   # 오른쪽
]


def show_board():
    """ 판 보여주기 """
    for row in board:
        print(row)
    print()


def DFS(row, col):
    """ 깊이 우선 탐색 """
    global board, copy_board
    copy_board = [row[:] for row in board]  # deepcopy
    stack = [(row, col)]

    while stack:
        crow, ccol = stack.pop()

        if visited[crow][ccol]:
            continue
        visited[crow][ccol] = True
        melting_count = 0

        for trow, tcol in MOVES:
            nrow, ncol = trow + crow, tcol + ccol
            if not (0 <= nrow < ROW and 0 <= ncol < COL):
                continue
            elif board[nrow][ncol] == 0:
                melting_count += 1
                continue
            elif visited[nrow][ncol]:
                continue
            stack.append((nrow, ncol))

        copy_board[crow][ccol] = max(copy_board[crow][ccol] - melting_count, 0)

    board = copy_board
    return 1


def find_ice():
    """ 첫번째 빙산 찾기 """
    global visited
    visited = [[False for _ in range(COL)] for _ in range(ROW)]
    ice_count = 0
    for row in range(ROW):
        for col in range(COL):
            if visited[row][col]:
                continue
            if board[row][col] == 0:
                visited[row][col] = True
                continue
            ice_count += DFS(row, col)
    return ice_count

def main():
    time = 0
    while True:
        ice_count = find_ice()

        if ice_count == 0:
            print(0)
            break

        if ice_count >= 2:
            print(time)
            break

        time += 1


if __name__ == '__main__':
    input = open('./test1.txt')
    # 판
    ROW, COL = map(int, input.readline().split())
    board = [list(map(int, input.readline().split())) for _ in range(ROW)]
    copy_board = []  # 판의 정보
    visited = []  # 방문 처리
    main()
