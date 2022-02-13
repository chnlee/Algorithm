n = int(input())
gamepan = [[0] * (n+1) for i in range(n+1)]
# 회전하는 정보
info = []
k = int(input())
for i in range(k):
  a, b = map(int,input().split())
  gamepan[a][b] = 1

l = int(input())
for i in range(l):
  x, c = input().split()
  info.append((int(x),c))

#동, 남, 서, 북 순서대로 방향 표시
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def move(direction, c):
  if c == 'L':
    direction = (direction-1) % 4
  else:
    direction = (direction+1) % 4
  return direction

def solution():  
  # 뱀의 위치를 2로 표현한다
  x, y = 1, 1
  gamepan[x][y] = 2
  q = [(x,y)]
  index = 0
  time = 0
  direction = 0
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and gamepan[nx][ny] != 2:
      if gamepan[nx][ny] == 0:
        gamepan[nx][ny] = 2
        q.append((nx,ny))
        px, py = q.pop(0)
        gamepan[px][py] = 0
      if gamepan[nx][ny] == 1:
        gamepan[nx][ny] = 2
        q.append((nx,ny))
    else:
      time += 1
      break
    x, y = nx, ny
    time += 1
    if index < l and time == info[index][0]:
      direction = move(direction,info[index][1])
      index += 1
  return print(time)

solution()





