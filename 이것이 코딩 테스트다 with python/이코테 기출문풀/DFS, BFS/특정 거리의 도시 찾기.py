# visited 대신 distance를 썼으면 훨씬 효율적으로 접근이 가능했던 문제.
# from collections import deque

# N, M, K, X = map(int,input().split())
# graph = [[] for i in range(N+1)]
# for i in range(M):
#   a, b = map(int,input().split())
#   graph[a].append(b)
# visited = [False] * (N+1)
# city = [[] for i in range(N+1)]
# def bfs(graph,start,visited):
#   visited[start] = True
#   count = 0
#   queue = deque([start])
#   while queue:
#     v = queue.popleft()
#     count += 1
#     for i in graph[v]:
#       if not visited[i]:
#         city[i].append(count)
#         queue.append(i)
#         visited[i] = True

# bfs(graph,X,visited)


# for i in range(N+1):
#   if K in city[i]:
#     print(i)
#     exit()
# print(-1)

# 그래프에서 모든 간선의 비용이 동일할 땐 너비 우선 탐색을 이용해서 찾을 수 있다. 
from collections import deque

N, M, K, X = map(int,input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
  a, b = map(int,input().split())
  graph[a].append(b)
distance = [-1] * (N+1)
distance[X] = 0
def bfs(graph,start,distance):
  queue = deque([start])
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if distance[i] == -1:  
        queue.append(i)
        distance[i] = distance[v] + 1

bfs(graph,X,distance)

check = False
for i in range(N+1):
  if distance[i] == K:
    print(i)
    check =True

if check == False:
  print(-1)

