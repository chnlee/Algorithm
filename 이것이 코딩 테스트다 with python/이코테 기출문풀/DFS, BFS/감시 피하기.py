
# 내가 생각한 풀이는 recursive한 특징을 이용해 장애물을 설치하는 것이였는데, 이상하게 계속 시간초과가 발생해 애를 먹었다.

# N = int(input())
# graph = []
# teachers = []
# for i in range(N):
#   graph.append(list(input().split()))
#   for j in range(N):
#     if graph[i][j] == 'T':
#       teachers.append((i,j))

# def check_obstacle(x,y,direction):
#   if direction == 0:
#     while y >= 0:
#       if graph[x][y] == 'S':
#         return True
#       if graph[x][y] == 'O':
#         return False
#       y -= 1
#   if direction == 1:
#     while y < N:
#       if graph[x][y] == 'S':
#         return True
#       if graph[x][y] == 'O':
#         return False
#       y += 1
#   if direction == 2:
#     while x >= 0:
#       if graph[x][y] == 'S':
#         return True
#       if graph[x][y] == 'O':
#         return False
#       x -= 1
#   if direction == 3:
#     while x < N:
#       if graph[x][y] == 'S':
#         return True
#       if graph[x][y] == 'O':
#         return False
#       x += 1
#   return False

# def process():
#   for x, y in teachers:
#         for direction in range(4):
#           if check_obstacle(x,y,direction):
#             return True
#   return False

# find = False

# def recursive(obstacle):
#   global find
#   if obstacle == 3:
#     if not process():
#       find = True
#       return
  
#   for i in range(N):
#     for j in range(N): 
#       if graph[i][j] == 'X':
#         obstacle += 1
#         graph[i][j] = 'O'
#         recursive(obstacle)
#         graph[i][j] = 'X'
#         obstacle -= 1

# recursive(0)

# if find:
#   print('YES')
# else:
#   print('NO')

from itertools import combinations

N = int(input())
graph = []
teachers = []
spaces = []
for i in range(N):
  graph.append(list(input().split()))
  for j in range(N):
    if graph[i][j] == 'T':
      teachers.append((i,j))
    if graph[i][j] == 'X':
      spaces.append((i,j))

def check_obstacle(x,y,direction):
  if direction == 0:
    while y >= 0:
      if graph[x][y] == 'S':
        return True
      if graph[x][y] == 'O':
        return False
      y -= 1
  if direction == 1:
    while y < N:
      if graph[x][y] == 'S':
        return True
      if graph[x][y] == 'O':
        return False
      y += 1
  if direction == 2:
    while x >= 0:
      if graph[x][y] == 'S':
        return True
      if graph[x][y] == 'O':
        return False
      x -= 1
  if direction == 3:
    while x < N:
      if graph[x][y] == 'S':
        return True
      if graph[x][y] == 'O':
        return False
      x += 1
  return False

def process():
  for x, y in teachers:
        for direction in range(4):
          if check_obstacle(x,y,direction):
            return True
  return False

find = False

for data in combinations(spaces,3):
  for x, y in data:
    graph[x][y] = 'O'
  if not process():
    find = True
    break
  for x,y in data:
    graph[x][y] = 'X'

if find:
  print('YES')
else:
  print('NO')


