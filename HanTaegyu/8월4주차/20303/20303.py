"""
    Solution code for "BaekJoon 할로윈의 양아치".

    - Problem link: https://www.acmicpc.net/problem/20303

    입력

    출력

"""
from sys import stdin as input
from collections import defaultdict
from typing import List


def find(node: int) -> None:
    if parents[node] == node:
        return parents[node]
    parents[node] = find(parents[node])
    return parents[node]


def union(node1: int, node2: int) -> int:
    parent1, parent2 = find(node1), find(node2)

    if parent1 < parent2:
        parents[parent2] = parents[parent1]
    elif parent2 < parent1:
        parents[parent1] = parents[parent2]
    return parent1


def show_board(data: List[List[int]]) -> None:
    for row in data:
        print(*row)


def main() -> None:
    """ 메인함수 """
    group = defaultdict(lambda: [0, 0])

    for node in range(people_count):
        root_node = find(node)
        group[root_node][0] += 1
        group[root_node][1] += candy[node]

    dp = [[0 for _ in range(crying_maximum)] for _ in range(len(group.keys()))]

    for index, (_, (personnel, candy_count)) in enumerate(group.items()):
        for count in range(1, crying_maximum):
            if count < personnel:
                dp[index][count] = dp[index - 1][count]
            else:
                dp[index][count] = max(
                    dp[index - 1][count - personnel] + candy_count,
                    dp[index - 1][count]
                )

    print(dp[-1][-1], end="")

if __name__ == '__main__':
    input = open('./test1.txt')
    people_count, relationship_count, crying_maximum = map(int, input.readline().split())
    candy = list(map(int, input.readline().split()))
    parents = [i for i in range(people_count)]

    for _ in range(relationship_count):
        node1, node2 = map(lambda x: int(x) - 1, input.readline().split())
        union(node1, node2)

    main()