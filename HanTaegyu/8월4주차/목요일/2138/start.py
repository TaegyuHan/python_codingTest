"""
    Solution code for "BaekJoon 전구와 스위치".

    - Problem link: https://www.acmicpc.net/problem/2138

    입력

    출력

"""
import sys
from sys import stdin as input
from typing import List


def switch(index: int, bulbs: List[int]) -> None:
    for i in range(index - 1, index + 2):
        if not (0 <= i < N):
            continue
        bulbs[i] = 1 - bulbs[i]
    # print(index, bulbs)


def change():
    tmp = start[:]  # copy
    answer = 0
    for i in range(1, N):
        if tmp[i - 1] == end[i - 1]:
            continue
        answer += 1
        switch(i, tmp)

    return answer if tmp == end else float("inf")


def main():
    """ 메인함수 """
    # 첫번째 스위치 X
    answer = change()

    # 첫번째 스위치 O
    switch(0, start)
    answer = min(answer, change() + 1)
    print(answer)


if __name__ == '__main__':
    # input = open('./test1.txt')
    N = int(input.readline())
    start = list(map(int, input.readline().strip()))
    end = list(map(int, input.readline().strip()))
    main()
