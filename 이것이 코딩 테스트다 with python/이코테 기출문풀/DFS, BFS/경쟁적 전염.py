# data 라는 리스트를 만들고, 바이러스 값, 시간, 위치 값을 넣는 것이 핵심이다.


from collections import deque

N, K = map(int,input().split())
graph = []
data = [] 
for i in range(N):
  graph.append(list(map(int,input().split())))
  for j in range(N):
    if graph[i][j] != 0:
      data.append((graph[i][j],0,i,j))

S, X, Y = map(int,input().split())

data.sort()
q = deque(data)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
  virus, s, x, y = q.popleft()
  if s == S:
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and nx < N and ny >=0 and ny < N:  
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus,s+1,nx,ny))

print(graph[X-1][Y-1])    


