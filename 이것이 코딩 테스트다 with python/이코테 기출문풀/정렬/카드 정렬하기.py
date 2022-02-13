# 우선순위 큐를 이용하는 문제!
# 우선순위 큐는 data가 들어왔을 때 정렬하는 특징을 가지고 있다.

import heapq

n = int(input())
q = []
for i in range(n):
  data = int(input())
  heapq.heappush(q,data)
result = 0
for i in range(n-1):
  temp1 = heapq.heappop(q)
  temp2 = heapq.heappop(q)
  temp = temp1+temp2
  heapq.heappush(q,temp)
  result += temp
print(result)