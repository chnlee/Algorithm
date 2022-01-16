# 무지의 먹방라이브
# 우선순위 큐를 이용한 문제 
# 복잡한 아이디어를 어떻게 구현하느냐가 관건임

import heapq

def solution(food_times,k):
  if sum(food_times) <= k:
    return -1
  q = []
  for i in range(len(food_times)):
    heapq.heappush(q,(food_times[i],i+1))
  # 총합 구하기
  sum_value = 0
  # 이전 값
  previous = 0
  # 현재 food_times의 길이
  length = len(food_times)
  # q[0][0] = food time이 가장 짧은 큐가 앞에 있음
  # now = 가장 짧은 큐를 빼는 용도(다음 큐가 앞으로 이동)
  # previous = 이미 뺀 짧은 큐 = now 가 된다.
  while (sum_value + (q[0][0]-previous)*length) <= k:
    now = heapq.heappop(q)[0]
    sum_value += (now-previous) * length
    previous = now
    length -= 1
  
  result = sorted(q,key=lambda x : x[1])
  answer = result[(k-sum_value)][1]

  return answer