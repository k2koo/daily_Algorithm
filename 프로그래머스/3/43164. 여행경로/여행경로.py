from collections import defaultdict

def solution(tickets):
    # 그래프를 딕셔너리로 생성, 각 출발지에 대해 도착지 리스트를 저장
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    
    # 도착지 리스트를 알파벳 순서로 정렬
    for key in graph:
        graph[key].sort(reverse=True)  # 나중에 pop()을 사용할 것이므로 reverse=True로 정렬
    
    route = []  # 경로를 저장할 리스트
    
    def dfs(airport):
        # 현재 공항에서 가능한 도착지로 이동
        while graph[airport]:
            next_airport = graph[airport].pop()  # 도착지 중 가장 알파벳 순서가 앞서는 곳으로 이동
            dfs(next_airport)  # 재귀적으로 다음 공항을 탐색
        route.append(airport)  # 더 이상 갈 곳이 없으면 경로에 추가
    
    dfs("ICN")  # 항상 "ICN"에서 출발
    
    return route[::-1]  # DFS 탐색이 끝나면 역순으로 경로를 반환
