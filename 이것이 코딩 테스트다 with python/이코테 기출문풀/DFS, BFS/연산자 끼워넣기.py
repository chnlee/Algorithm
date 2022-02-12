# 각 사칙 연산에 대해서 회귀적으로 사용하는 문제.
# 즉, dfs를 이용해서 풀 수 있었다.
N = int(input())
Numbers = list(map(int,input().split()))
Operators = list(map(int,input().split()))
max_value = -1e9
min_value = 1e9
def dfs(num, now):
  global min_value, max_value
  if num == len(Numbers) :
    min_value = min(min_value,now)
    max_value = max(max_value,now)
  else:
    if Operators[0] > 0:
      Operators[0] -= 1
      dfs(num+1, now + Numbers[num])
      Operators[0] += 1
    if Operators[1] > 0:
      Operators[1] -= 1
      dfs(num+1, now - Numbers[num])
      Operators[1] += 1
    if Operators[2] > 0:
      Operators[2] -= 1
      dfs(num+1, now * Numbers[num])
      Operators[2] += 1
    if Operators[3] > 0:
      Operators[3] -= 1
      dfs(num+1, int(now / Numbers[num]))
      Operators[3] += 1

dfs(1,Numbers[0])

print(max_value)
print(min_value)



