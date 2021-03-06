# virus 함수, get_score()함수, dfs 함수 모두 만들어야함
# 특히 count를 기준으로 하는 dfs 함수 작성 방법이 매우 
n, m = map(int,input().split())
result = 0
temp = [[0] * m for i in range(n)]
data = []
for i in range(n):
  data.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def virus(x,y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
      if temp[nx][ny] == 0:
        temp[nx][ny] = 2
        virus(nx,ny)

def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1
  return score

def dfs(count):
  global result
  if count == 3 :
    for i in range(n):
      for j in range(m):
        temp[i][j] = data[i][j]
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i,j)
    score = get_score()
    result = max(result,score)
    return
  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs(count)
        data[i][j] = 0
        count -= 1

dfs(0)
print(result)
