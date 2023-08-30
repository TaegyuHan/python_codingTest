"""
    Solution code for "BaekJoon 이모티콘".

    - Problem link: https://www.acmicpc.net/problem/14226

    입력
        (2 ≤ S ≤ 1000)

    출력
        정수
"""
from sys import stdin as input
from collections import deque


def main():
    """ 메인함수 """
    visited = set()
    queue = deque([(1, 0, 0)])

    while queue:
        screen, clipboard, time = queue.popleft()

        if (screen, clipboard) in visited:  # 이미 방문한 상태인 경우 스킵
            continue
        visited.add((screen, clipboard))

        if screen == target_count:
            print(time, end="")
            break

        time += 1

        # 1 : 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
        if (screen, screen) not in visited:
            queue.append((screen, screen, time))

        # 2 : 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
        if (screen + clipboard, clipboard) not in visited:
            queue.append((screen + clipboard, clipboard, time))

        # 3 : 화면에 있는 이모티콘 중 하나를 삭제한다.
        if (screen - 1, clipboard) not in visited or (screen - 1) < 0:
            queue.append((screen - 1, clipboard, time))


if __name__ == '__main__':
    input = open('./test4.txt')
    target_count = int(input.readline())
    main()