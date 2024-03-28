from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0]) 
    visited = [[False] * m for _ in range(n)]

    # 상, 하, 좌, 우 방향 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # BFS를 위한 큐 초기화 및 시작 위치 설정
    queue = deque([(0, 0, 1)])  # (x, y, 이동 횟수)
    visited[0][0] = True

    while queue:
        x, y, count = queue.popleft()

        # 상대 팀 진영에 도착한 경우
        if x == n - 1 and y == m - 1:
            return count  # 현재까지의 이동 횟수 반환

        # 상하좌우 방향으로의 이동 시도
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 맵의 범위를 벗어나지 않고, 벽이 없으며, 아직 방문하지 않은 칸인 경우
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))

    # 상대 팀 진영에 도착할 수 없는 경우
    return -1