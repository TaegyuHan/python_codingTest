"""
    Solution code for "BaekJoon 두 로봇".

    - Problem link: https://www.acmicpc.net/problem/15971

    입력

    출력

"""
from sys import stdin as input
from collections import defaultdict, deque
from typing import List


def visited_reset(visited: List[bool]) -> List[bool]:
    """ 방문 리셋 """
    for i in range(len(visited)):
        visited[i] = False
    return visited


def bfs(visited, save_data, start):
    """ 프로그램 """
    queue = deque([(start, 0)])

    while queue:
        node, weight = queue.popleft()

        if visited[node]: continue
        visited[node] = True
        save_data[node] = weight

        for nnode, nweight in nodes[node]:
            if visited[nnode]: continue
            queue.append((nnode, nweight + weight))


def find_min() -> int:
    answer = save_red_nodes[blue_node]
    for node in range(node_count):
        for nnode, _ in nodes[node]:
            answer = min(answer, save_blue_node[nnode] + save_red_nodes[node])
    return answer


def main() -> None:
    """ 메인함수 """
    global visited
    visited = visited_reset(visited)
    bfs(visited, save_red_nodes, red_node)

    visited = visited_reset(visited)
    bfs(visited, save_blue_node, blue_node)

    answer = find_min()
    print(answer, end="")


if __name__ == '__main__':
    # input = open('./test2.txt')
    node_count, red_node, blue_node = map(lambda x: int(x) - 1, input.readline().split())
    node_count += 1

    nodes = defaultdict(list)
    for _ in range(node_count - 1):
        node1, node2, weight = map(lambda x: int(x) - 1, input.readline().split())
        weight += 1
        nodes[node1].append((node2, weight))
        nodes[node2].append((node1, weight))

    visited = [False for _ in range(node_count)]
    save_red_nodes = [0 for _ in range(node_count)]
    save_blue_node = [0 for _ in range(node_count)]
    main()