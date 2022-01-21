#참고하면서 풀었다. 
#combination을 알아야 수월한 문제.
from itertools import combinations

n, m = map(int,input().split())
chicken, house = [], []
for r in range(n):
  data = list(map(int,input().split()))
  for c in range(n):
    if data[c] == 1:
      house.append((r+1,c+1))
    elif data[c] == 2:
      chicken.append((r+1,c+1))

candidates = list(combinations(chicken,m))

def get_sum(candidate):
  sum = 0
  for home in house:
    ax, ay = home
    temp = 1e9
    for bx,by in candidate:
     temp = min(temp, abs(ax-bx) + abs(ay-by))
    sum += temp
  return sum

result = 1e9
for candidate in candidates:
  result = min( result , get_sum(candidate))
print(result)

